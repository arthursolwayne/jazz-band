
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics and rhythmic variation
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: Dm7 -> F -> Bb -> C -> Dm7
# Dm7 = D, F, A, C
# F = F
# Bb = Bb
# C = C
# End with Dm7 again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # C
]
sax.notes.extend(sax_notes)

# Bass line: Walking in Dm with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=1.875),  # Bb#
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=2.375, end=2.5),  # Bb#
    pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.625),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.125),  # Bb#
    pretty_midi.Note(velocity=80, pitch=63, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # C
]
piano.notes.extend(piano_notes)

# Drums in bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=60, pitch=36, start=1.5, end=1.625),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=36, start=2.25, end=2.375),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.625),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=60, pitch=36, start=3.0, end=3.125),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=3.25, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=36, start=3.75, end=3.875),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.125),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=60, pitch=36, start=4.5, end=4.625),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=4.75, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=36, start=5.25, end=5.375),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.625),  # Snare on 4
]
for note in drum_notes:
    dr = pretty_midi.Note(note.velocity, note.pitch, note.start, note.end)
    drums.notes.append(dr)

# Add hihat on every eighth, with some dynamic shading
for i in range(1.5, 6.0, 0.1875):
    if i % 1.0 < 0.9375:
        velocity = 90
    else:
        velocity = 85
    hihat = pretty_midi.Note(velocity=velocity, pitch=42, start=i, end=i + 0.1875)
    drums.notes.append(hihat)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
