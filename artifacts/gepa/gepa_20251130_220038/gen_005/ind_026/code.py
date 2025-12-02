
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
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm motif - F, Ab, Bb, D
note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Fm
note5 = pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.75)  # F
note6 = pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0)  # Gb
note7 = pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25)  # E
note8 = pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5)  # Ab
bass.notes.extend([note5, note6, note7, note8])

# Piano: 7th chords on 2 and 4
note9 = pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)  # F7 - F
note10 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0) # F7 - A
note11 = pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0) # F7 - C
note12 = pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0) # F7 - Eb
note13 = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5) # F7 - F
note14 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5) # F7 - A
note15 = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5) # F7 - C
note16 = pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5) # F7 - Eb
piano.notes.extend([note9, note10, note11, note12, note13, note14, note15, note16])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
drum_hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_kick2, drum_kick3, drum_snare2, drum_snare3, drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with variation
note17 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)
note18 = pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5)
note19 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
note20 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)
sax.notes.extend([note17, note18, note19, note20])

# Bass: Walking line
note21 = pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25)  # Bb
note22 = pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5)  # B
note23 = pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75)  # A
note24 = pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0)  # D
bass.notes.extend([note21, note22, note23, note24])

# Piano: 7th chords on 2 and 4
note25 = pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5)  # Bb7 - Bb
note26 = pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5) # Bb7 - D
note27 = pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5) # Bb7 - F
note28 = pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5) # Bb7 - Ab
note29 = pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0) # Bb7 - Bb
note30 = pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.0) # Bb7 - D
note31 = pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0) # Bb7 - F
note32 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0) # Bb7 - Ab
piano.notes.extend([note25, note26, note27, note28, note29, note30, note31, note32])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick5 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_snare5 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
drum_hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_kick4, drum_kick5, drum_snare4, drum_snare5, drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a resolution
note33 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)
note34 = pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0)
note35 = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)
note36 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)
note37 = pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75)
note38 = pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0)
sax.notes.extend([note33, note34, note35, note36, note37, note38])

# Bass: Walking line
note39 = pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75)  # D
note40 = pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0)  # Eb
note41 = pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25)  # Bb
note42 = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5)  # F
note43 = pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75)  # Ab
note44 = pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0)  # Bb
bass.notes.extend([note39, note40, note41, note42, note43, note44])

# Piano: 7th chords on 2 and 4
note45 = pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0)  # Ab7 - Ab
note46 = pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0) # Ab7 - C
note47 = pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0) # Ab7 - Eb
note48 = pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0) # Ab7 - F
note49 = pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75) # Ab7 - Ab
note50 = pretty_midi.Note(velocity=90, pitch=63, start=5.5, end=5.75) # Ab7 - C
note51 = pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75) # Ab7 - Eb
note52 = pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75) # Ab7 - F
piano.notes.extend([note45, note46, note47, note48, note49, note50, note51, note52])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick6 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick7 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drum_snare6 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_snare7 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
drum_hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_kick6, drum_kick7, drum_snare6, drum_snare7, drum_hihat13, drum_hihat14, drum_hihat15, drum_hihat16])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
