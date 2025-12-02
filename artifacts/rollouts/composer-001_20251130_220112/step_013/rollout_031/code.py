
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),     # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),     # D (root)
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),    # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),    # F (3rd)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),     # G (5th)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),     # A (7th)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),    # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),    # A (7th)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),     # G (5th)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),     # F (3rd)
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),    # E (chromatic)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),    # D (root)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),     # C (chromatic)
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),     # G (root)
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),     # B (7th)
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),     # D (9th)
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),     # F# (11th)

    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),    # G (root)
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),    # B (7th)
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),    # D (9th)
    pretty_midi.Note(velocity=95, pitch=77, start=2.25, end=2.625),    # F# (11th)

    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),    # G (root)
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.125),    # B (7th)
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.125),    # D (9th)
    pretty_midi.Note(velocity=95, pitch=77, start=3.75, end=4.125),    # F# (11th)

    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),     # G (root)
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),     # B (7th)
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875),     # D (9th)
    pretty_midi.Note(velocity=95, pitch=77, start=4.5, end=4.875),     # F# (11th)
]
piano.notes.extend(piano_notes)

# Dante on sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),    # E (3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),   # A (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),    # A (7th)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),    # E (3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),   # A (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),   # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),    # A (7th)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),    # E (3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),   # A (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),   # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),    # A (7th)
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
