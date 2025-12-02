
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

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0), # A
]

# Diane: Comp on 2 and 4 with 7th chords
chord1 = pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25) # F7 - F
chord2 = pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25) # F7 - Bb
chord3 = pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25) # F7 - C
chord4 = pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25) # F7 - Db
chord5 = pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375) # F7 - F
chord6 = pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375) # F7 - Bb
chord7 = pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375) # F7 - C
chord8 = pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375) # F7 - Db

piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8])

# Dante: Motif - F, G, Ab, A (start at 1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # A
]

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in F (Bb, B, C, Db, D, Eb, E, F)
bass_notes2 = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5), # Db
]

# Diane: Comp on 2 and 4 with 7th chords
chord9 = pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75) # F7 - F
chord10 = pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75) # F7 - Bb
chord11 = pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75) # F7 - C
chord12 = pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75) # F7 - Db
chord13 = pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875) # F7 - F
chord14 = pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875) # F7 - Bb
chord15 = pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875) # F7 - C
chord16 = pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875) # F7 - Db

piano.notes.extend([chord9, chord10, chord11, chord12, chord13, chord14, chord15, chord16])

# Dante: Motif variation - Ab, A, Bb, B (start at 3.0s)
sax_notes2 = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5), # B
]

sax.notes.extend(sax_notes2)
bass.notes.extend(bass_notes2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in F (D, Eb, E, F)
bass_notes3 = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0), # F
]

# Diane: Comp on 2 and 4 with 7th chords
chord17 = pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25) # F7 - F
chord18 = pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25) # F7 - Bb
chord19 = pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25) # F7 - C
chord20 = pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25) # F7 - Db
chord21 = pretty_midi.Note(velocity=95, pitch=64, start=6.0, end=6.375) # F7 - F
chord22 = pretty_midi.Note(velocity=95, pitch=69, start=6.0, end=6.375) # F7 - Bb
chord23 = pretty_midi.Note(velocity=95, pitch=71, start=6.0, end=6.375) # F7 - C
chord24 = pretty_midi.Note(velocity=95, pitch=72, start=6.0, end=6.375) # F7 - Db

piano.notes.extend([chord17, chord18, chord19, chord20, chord21, chord22, chord23, chord24])

# Dante: Motif return - F, G, Ab, A (start at 4.5s)
sax_notes3 = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # A
]

sax.notes.extend(sax_notes3)
bass.notes.extend(bass_notes3)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)

kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat9 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat10 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat11 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat12 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick3, snare2, hihat5, hihat6, hihat7, hihat8, kick4, kick5, snare3, hihat9, hihat10, hihat11, hihat12, kick6])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
