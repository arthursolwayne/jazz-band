
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=39, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5),  # Ab
    # Repeat last two measures
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # D
    # Bar 3 - Cm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # Bb
    # Bar 4 - F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.25),  # D
    # Bar 5 - Cm7 on 2 and 4 (repeat last measure)
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # Bb
]
piano.notes.extend(piano_notes)

# Dante on sax - the melody
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # F
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=3.0, end=3.25),  # E
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # F
    # Bar 5 - Repeat the motif with a twist
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Add the drum pattern for bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)

# Append the new notes to the drum instrument
drums.notes.extend([note for note in drums.notes if note not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
