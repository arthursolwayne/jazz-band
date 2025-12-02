
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

# Bass line - Marcus: walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),     # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),   # Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),   # E (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),    # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),    # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),   # G
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),   # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),    # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),    # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),   # A
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),   # G
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),    # F
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = []
# Bar 2 (1.5 - 3.0s)
piano_notes.append(pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875))  # F
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875))  # Bb
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875))  # D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875))  # Ab
# Bar 3 (3.0 - 4.5s)
piano_notes.append(pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375))  # F
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375))  # Bb
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375))  # D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375))  # Ab
# Bar 4 (4.5 - 6.0s)
piano_notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875))  # F
piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875))  # Bb
piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875))  # D
piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875))  # Ab
piano.notes.extend(piano_notes)

# Tenor sax - Dante: short motif, make it sing
# Motif: F (64), Bb (67), D (71), Ab (69) – Fm7 chord
# Play the first three notes in bar 2, leave the last note hanging
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=105, pitch=71, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=105, pitch=69, start=1.875, end=2.0),  # Ab
    # Repeat the motif in bar 4, ending on the full chord
    pretty_midi.Note(velocity=105, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=4.625, end=4.75), # Bb
    pretty_midi.Note(velocity=105, pitch=71, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=105, pitch=69, start=4.875, end=5.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
