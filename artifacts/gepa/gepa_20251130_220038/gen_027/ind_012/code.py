
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line with chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # Eb
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # Eb
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (melody in Fm, short motif)
# Motif: F (64), Ab (69), Bb (71), Eb (67) - 4 notes over 2 beats
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # Eb
    # Repeat the motif with a slight variation
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # Eb
    # Final iteration with a slight delay on last note
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
