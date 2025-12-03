
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F - G - D - C (F2, G2, D2, C2)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=69, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: F7, Bb7, D7, C7 (open voicings, resolve on the last)
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=75, pitch=76, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=75, pitch=71, start=2.25, end=2.625),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=80, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=84, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=82, start=2.625, end=3.0),
    pretty_midi.Note(velocity=75, pitch=79, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # A5
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0)   # A5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F - C - D - F (F2, C2, D2, F2)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=71, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: G7, C7, D7, F7 (open voicings, resolve on the last)
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=78, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=75, pitch=76, start=3.0, end=3.375),
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=79, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.125),
    pretty_midi.Note(velocity=75, pitch=81, start=3.75, end=4.125),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=80, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=84, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=82, start=4.125, end=4.5),
    pretty_midi.Note(velocity=75, pitch=79, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth (Bar 2-4)
for bar in [1, 2]:
    start = 1.5 + bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

# Bar 4: Sax continues (4.5 - 6.0s)
# Leave the motif hanging, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # F6
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # D6
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # F6
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D6
    pretty_midi.Note(velocity=100, pitch=77, start=5.5, end=5.75)   # G6
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
