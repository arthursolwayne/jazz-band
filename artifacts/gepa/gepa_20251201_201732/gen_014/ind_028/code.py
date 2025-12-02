
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4 (outside bar 1)
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Gb
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F Ab C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # Eb

    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Ab

    # Bar 4: C7 (C E G Bb)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Gb - Ab - C (Fm scale), but played with space and tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # C (resolution)
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # F (start)
    pretty_midi.Note(velocity=110, pitch=49, start=2.625, end=3.0),   # Gb
    pretty_midi.Note(velocity=110, pitch=47, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=4.125, end=4.5),   # C (return)
    pretty_midi.Note(velocity=110, pitch=50, start=4.875, end=5.25),  # F (finish)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
