
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (bass): Walking line in Fm, chromatic approaches
# Diane (piano): 7th chords on 2 and 4
# Dante (sax): Short motif, make it sing
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bass line (Fm)
# F - Gb - Ab - Bb - F - Gb - Ab - Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords on 2 and 4)
# Fm7 on 2 (1.875)
# Ab7 on 4 (2.625)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # Db
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Saxophone motif (F - Ab - Bb - F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Drums
kick_1b = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2b = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat_1b = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
hihat_2b = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
hihat_3b = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
hihat_4b = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
kick_3b = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drums.notes.extend([kick_1b, snare_2b, hihat_1b, hihat_2b, hihat_3b, hihat_4b, kick_3b])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line (Fm)
# F - Gb - Ab - Bb - F - Gb - Ab - Bb
bass_notes2 = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes2)

# Piano chords (7th chords on 2 and 4)
# Fm7 on 2 (3.375)
# Ab7 on 4 (4.125)
piano_notes2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # Db
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes2)

# Saxophone motif (Ab - F - Bb - Ab)
sax_notes2 = [
    pretty_midi.Note(velocity=110, pitch=51, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=51, start=4.125, end=4.5),  # Ab
]
sax.notes.extend(sax_notes2)

# Drums
kick_1c = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_2c = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat_1c = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
hihat_2c = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat_3c = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat_4c = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
kick_3c = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.extend([kick_1c, snare_2c, hihat_1c, hihat_2c, hihat_3c, hihat_4c, kick_3c])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line (Fm)
# F - Gb - Ab - Bb - F - Gb - Ab - Bb
bass_notes3 = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes3)

# Piano chords (7th chords on 2 and 4)
# Fm7 on 2 (4.875)
# Ab7 on 4 (5.625)
piano_notes3 = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # Db
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes3)

# Saxophone motif (Bb - F - Ab - Bb)
sax_notes3 = [
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes3)

# Drums
kick_1d = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_2d = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat_1d = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
hihat_2d = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat_3d = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat_4d = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
kick_3d = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([kick_1d, snare_2d, hihat_1d, hihat_2d, hihat_3d, hihat_4d, kick_3d])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
