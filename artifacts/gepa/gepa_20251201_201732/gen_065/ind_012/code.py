
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
# Bar 2: D (MIDI 38)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.0)
bass.notes.append(note)
# Bar 3: G (MIDI 43)
note = pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.5)
bass.notes.append(note)
# Bar 4: D (MIDI 38) with chromatic approach from C# (MIDI 37)
note = pretty_midi.Note(velocity=100, pitch=37, start=2.5, end=2.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: D9 (D, F#, A, C#, E)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)
note4 = pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0)
note5 = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0)
piano.notes.extend([note1, note2, note3, note4, note5])

# Bar 3: G7 (G, B, D, F)
note1 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5)
note2 = pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5)
note3 = pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5)
note4 = pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5)
piano.notes.extend([note1, note2, note3, note4])

# Bar 4: Dmaj7 (D, F#, A, C#)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0)
note3 = pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0)
note4 = pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0)
piano.notes.extend([note1, note2, note3, note4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Bar 2: Start the motif
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75)
sax.notes.append(note)
# Bar 3: Leave it hanging
note = pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25)
sax.notes.append(note)
# Bar 4: Finish it
note = pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
