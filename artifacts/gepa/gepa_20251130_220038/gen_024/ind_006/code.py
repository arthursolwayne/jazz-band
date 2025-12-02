
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=100, pitch=83, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=84, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=86, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.25),  # F7 (Bb)
    # Bar 3 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75),  # F7 (Bb)
    # Bar 4 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25),  # F7 (Bb)
]
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. F7 chord
sax_notes = [
    # Bar 2 - Start motif
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=2.625, end=3.0),  # F
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75),  # F
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Add remaining drum fills
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),  # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
