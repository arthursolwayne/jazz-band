
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
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax - motif starts here
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)  # E
sax_note_2 = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)  # A
sax_note_3 = pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25)  # Bb
sax_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)  # E
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Bass - walking line
bass_note_1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75)  # F
bass_note_2 = pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0)  # G
bass_note_3 = pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25)  # Gb
bass_note_4 = pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5)  # F
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano - 7th chords on 2 and 4
piano_note_1 = pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)  # C (F7)
piano_note_2 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)  # E
piano_note_3 = pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0)  # G
piano_note_4 = pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0)  # Bb
piano_note_5 = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5)  # C (F7)
piano_note_6 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5)  # E
piano_note_7 = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5)  # G
piano_note_8 = pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5)  # Bb
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4, piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25)
hihat_5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat_6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat_7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
hihat_8 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick_2, snare_2, hihat_5, hihat_6, hihat_7, hihat_8])

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax - motif continues
sax_note_5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)  # A
sax_note_6 = pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5)  # D
sax_note_7 = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)  # Eb
sax_note_8 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)  # A
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Bass - walking line
bass_note_5 = pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25)  # A
bass_note_6 = pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5)  # Bb
bass_note_7 = pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75)  # A
bass_note_8 = pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0)  # Ab
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano - 7th chords on 2 and 4
piano_note_9 = pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5)  # E (A7)
piano_note_10 = pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5)  # G
piano_note_11 = pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5)  # B
piano_note_12 = pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5)  # D
piano_note_13 = pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0)  # E (A7)
piano_note_14 = pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0)  # G
piano_note_15 = pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0)  # B
piano_note_16 = pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0)  # D
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12, piano_note_13, piano_note_14, piano_note_15, piano_note_16])

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_3 = pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75)
hihat_9 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat_10 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat_11 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat_12 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick_3, snare_3, hihat_9, hihat_10, hihat_11, hihat_12])

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax - motif resolves
sax_note_9 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)  # F
sax_note_10 = pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0)  # A
sax_note_11 = pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25)  # Bb
sax_note_12 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)  # A
sax_note_13 = pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75)  # F
sax_note_14 = pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)  # E
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12, sax_note_13, sax_note_14])

# Bass - walking line
bass_note_9 = pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.75)  # Ab
bass_note_10 = pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0)  # A
bass_note_11 = pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.25)  # G
bass_note_12 = pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5)  # Gb
bass_note_13 = pretty_midi.Note(velocity=80, pitch=59, start=5.5, end=5.75)  # Ab
bass_note_14 = pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0)  # Gb
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12, bass_note_13, bass_note_14])

# Piano - 7th chords on 2 and 4
piano_note_17 = pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0)  # C (F7)
piano_note_18 = pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0)  # E
piano_note_19 = pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0)  # G
piano_note_20 = pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0)  # Bb
piano_note_21 = pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75)  # C (F7)
piano_note_22 = pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75)  # E
piano_note_23 = pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75)  # G
piano_note_24 = pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75)  # Bb
piano.notes.extend([piano_note_17, piano_note_18, piano_note_19, piano_note_20, piano_note_21, piano_note_22, piano_note_23, piano_note_24])

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25)
hihat_13 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat_14 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat_15 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat_16 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick_4, snare_4, hihat_13, hihat_14, hihat_15, hihat_16])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
