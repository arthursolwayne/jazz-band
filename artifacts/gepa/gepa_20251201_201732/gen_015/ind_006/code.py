
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F - Ab - D - C)
# Bar 2: F (1.5 - 1.875), Ab (1.875 - 2.25), D (2.25 - 2.625), C (2.625 - 3.0)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),
    # Bar 3: Ab (3.0 - 3.375), D (3.375 - 3.75), C (3.75 - 4.125), F (4.125 - 4.5)
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),
    # Bar 4: D (4.5 - 4.875), C (4.875 - 5.25), F (5.25 - 5.625), Ab (5.625 - 6.0)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Gb7 (Gb, Bb, Db, F)
# Bar 4: Am7 (A, C, E, G)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=1.5, end=1.875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # Db
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
]
piano.notes.extend(piano_notes)

# Dante: Sax motif. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C (1.5 - 1.875), then rest (1.875 - 2.25), then F - Bb - C again (2.25 - 2.625)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0)
]
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5)
]
# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(bar2_drum_notes + bar3_drum_notes + bar4_drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
