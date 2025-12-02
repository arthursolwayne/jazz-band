
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: C E D G (Cmaj7), then Bb D C F (Bbmaj7)
note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: walking line in C, chromatic approaches
note5 = pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75)
note6 = pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0)
note7 = pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25)
note8 = pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5)
bass.notes.extend([note5, note6, note7, note8])

# Piano: 7th chords, comp on 2 and 4
note9 = pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)  # C
note10 = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0) # E
note11 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0) # G
note12 = pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0) # B
note13 = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5) # C
note14 = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5) # E
note15 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5) # G
note16 = pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5) # Bb
piano.notes.extend([note9, note10, note11, note12, note13, note14, note15, note16])

# Drums: Bar 2
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick, snare, hihat])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Bb D C F (Bbmaj7)
note17 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25)
note18 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
note19 = pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75)
note20 = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
sax.notes.extend([note17, note18, note19, note20])

# Bass: walking line in C, chromatic approaches
note21 = pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.25)
note22 = pretty_midi.Note(velocity=100, pitch=52, start=3.25, end=3.5)
note23 = pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75)
note24 = pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.0)
bass.notes.extend([note21, note22, note23, note24])

# Piano: 7th chords, comp on 2 and 4
note25 = pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5)  # Bb
note26 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5) # D
note27 = pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5) # F
note28 = pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5) # Ab
note29 = pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0)  # Bb
note30 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0) # D
note31 = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0) # F
note32 = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0) # Ab
piano.notes.extend([note25, note26, note27, note28, note29, note30, note31, note32])

# Drums: Bar 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick, snare, hihat])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: C E D G (Cmaj7), then Bb D C F (Bbmaj7) — finish the phrase
note33 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75)
note34 = pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0)
note35 = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)
note36 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)
note37 = pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.75)
note38 = pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)
note39 = pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0)
note40 = pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0)
sax.notes.extend([note33, note34, note35, note36, note37, note38, note39, note40])

# Bass: walking line in C, chromatic approaches
note41 = pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.75)
note42 = pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0)
note43 = pretty_midi.Note(velocity=100, pitch=56, start=5.0, end=5.25)
note44 = pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.5)
note45 = pretty_midi.Note(velocity=100, pitch=58, start=5.5, end=5.75)
note46 = pretty_midi.Note(velocity=100, pitch=59, start=5.75, end=6.0)
bass.notes.extend([note41, note42, note43, note44, note45, note46])

# Piano: 7th chords, comp on 2 and 4
note47 = pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0)  # C
note48 = pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0) # E
note49 = pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0) # G
note50 = pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0) # B
note51 = pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.75)  # Bb
note52 = pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75) # D
note53 = pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75) # F
note54 = pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75) # Ab
piano.notes.extend([note47, note48, note49, note50, note51, note52, note53, note54])

# Drums: Bar 4
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick, snare, hihat])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
