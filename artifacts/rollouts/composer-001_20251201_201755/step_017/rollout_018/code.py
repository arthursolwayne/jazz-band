
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
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
# Bar 2: D (MIDI 38) -> F# (MIDI 41) -> G (MIDI 43) -> B (MIDI 46)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0))
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0))  # F#
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0))  # A
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0))  # C#
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Start with D (MIDI 62) on beat 1
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))
# Leave it hanging with a half-step up to E (MIDI 64) on beat 2
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25))
# Come back with a descending line to finish the motif in bar 4
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0))
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G (MIDI 43) -> A (MIDI 45) -> B (MIDI 47) -> D (MIDI 49)
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5))
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F)
piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5))  # G
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5))  # B
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5))  # F
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3
drum_notes = []
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
for i in range(0, 4):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: B (MIDI 47) -> C# (MIDI 49) -> D (MIDI 50) -> F# (MIDI 52)
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625))
bass_notes.append(pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0))
bass.notes.extend(bass_notes)

# Piano: Bm7 (B, D, F#, A)
piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0))  # B
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0))  # F#
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0))  # A
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4
drum_notes = []
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5))
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
