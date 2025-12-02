
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Fm b9
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # Fm b7
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Fm 9
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # Fm 11
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Fm 9
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # Fm root
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # Fm b7
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),  # Fm b9
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Fm 9
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Fm 11
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # Fm root
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25),  # Fm7: F (59)
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # Ab (55)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # C (62)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Db (60)
    # Bar 3 (beat 2)
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # Fm7
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # Db
    # Bar 4 (beat 2)
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25),  # Fm7
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (start of motif)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # Bb
    # Bar 3 (let it hang)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # Bb
    # Bar 4 (finish it)
    pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=59, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_4bar_intro.mid")
