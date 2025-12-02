
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # C
]
piano.notes.extend(piano_notes)

# Sax: motif starts on bar 2
sax_note_1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75)  # E
sax_note_2 = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)   # G
sax_note_3 = pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25)  # E
sax_note_4 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)  # A
sax_notes = [sax_note_1, sax_note_2, sax_note_3, sax_note_4]
sax.notes.extend(sax_notes)

# Bar 3: (3.0 - 4.5s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # C
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif
sax_note_5 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)  # G
sax_note_6 = pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5)   # E
sax_note_7 = pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75)   # A
sax_note_8 = pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0)   # C
sax_notes = [sax_note_5, sax_note_6, sax_note_7, sax_note_8]
sax.notes.extend(sax_notes)

# Bar 4: (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_kick2, drum_snare2, drum_hihat])

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # C
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_note_9 = pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75)  # G
sax_note_10 = pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0)  # E
sax_note_11 = pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25)  # A
sax_note_12 = pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5)  # E
sax_note_13 = pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75)  # G
sax_note_14 = pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0)  # E
sax_notes = [sax_note_9, sax_note_10, sax_note_11, sax_note_12, sax_note_13, sax_note_14]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
