
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (38), F# (41), G (43), D (38)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5)
bass.notes.append(note)

# Bar 3: A (45), C# (48), D (43), A (45)
note = pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=3.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.5)
bass.notes.append(note)

# Bar 4: D (38), F# (41), G (43), D (38)
note = pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=4.0, end=4.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.5)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#) -> C# diminished (C#, E, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3: A7 (A, C#, E, G#) -> G# diminished (G#, B, D, F)
note = pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=2.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=2.75)
piano.notes.append(note)

# Bar 4: D7 (D, F#, A, C#) -> C# diminished (C#, E, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.125, end=time + 0.25)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: D (62), E (64), F# (67), D (62)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
sax.notes.append(note)

# Bar 3: Rest
# Bar 4: D (62), E (64), F# (67), D (62)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
