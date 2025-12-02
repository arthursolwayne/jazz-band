
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
bar1_start = 0.0
bar1_end = 1.5
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start, end=bar1_end)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Sax: Fm motif - F, Ab, Bb, D
sax_note1 = pretty_midi.Note(velocity=100, pitch=53, start=bar2_start, end=bar2_start + 0.375)
sax_note2 = pretty_midi.Note(velocity=100, pitch=50, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375)
sax_note3 = pretty_midi.Note(velocity=100, pitch=52, start=bar2_start + 1.125, end=bar2_start + 1.125 + 0.375)
sax_note4 = pretty_midi.Note(velocity=100, pitch=57, start=bar2_start + 1.5, end=bar2_start + 1.5 + 0.375)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=50, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=47, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=53, start=bar2_start + 1.125, end=bar2_start + 1.5),
    pretty_midi.Note(velocity=80, pitch=50, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=48, start=bar2_start + 1.875, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=80, pitch=52, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=53, start=bar2_start + 2.625, end=bar2_start + 3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, F7 on 2, Bb7 on 4
piano_notes = [
    # F7 on beat 2 (bar 2)
    pretty_midi.Note(velocity=90, pitch=53, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=52, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=57, start=bar2_start + 0.75, end=bar2_start + 1.125),
    
    # Bb7 on beat 4 (bar 2)
    pretty_midi.Note(velocity=90, pitch=52, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=bar2_start + 1.5, end=bar2_start + 1.875)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar2_start, end=bar2_end)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Sax: Repeat the motif but an octave lower
sax_note5 = pretty_midi.Note(velocity=100, pitch=43, start=bar3_start, end=bar3_start + 0.375)
sax_note6 = pretty_midi.Note(velocity=100, pitch=40, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375)
sax_note7 = pretty_midi.Note(velocity=100, pitch=42, start=bar3_start + 1.125, end=bar3_start + 1.125 + 0.375)
sax_note8 = pretty_midi.Note(velocity=100, pitch=47, start=bar3_start + 1.5, end=bar3_start + 1.5 + 0.375)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bass: Walking line in Fm
bass_notes2 = [
    pretty_midi.Note(velocity=80, pitch=48, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=50, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=47, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=53, start=bar3_start + 1.125, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=80, pitch=50, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=48, start=bar3_start + 1.875, end=bar3_start + 2.25),
    pretty_midi.Note(velocity=80, pitch=52, start=bar3_start + 2.25, end=bar3_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=53, start=bar3_start + 2.625, end=bar3_start + 3.0)
]
bass.notes.extend(bass_notes2)

# Piano: 7th chords on 2 and 4, F7 on 2, Bb7 on 4
piano_notes2 = [
    # F7 on beat 2 (bar 3)
    pretty_midi.Note(velocity=90, pitch=53, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=52, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=57, start=bar3_start + 0.75, end=bar3_start + 1.125),
    
    # Bb7 on beat 4 (bar 3)
    pretty_midi.Note(velocity=90, pitch=52, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=49, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=bar3_start + 1.5, end=bar3_start + 1.875)
]
piano.notes.extend(piano_notes2)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar3_start, end=bar3_end)
drums.notes.extend([kick3, snare3, hihat3])

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Sax: Repeat the motif, descending by a whole step
sax_note9 = pretty_midi.Note(velocity=100, pitch=41, start=bar4_start, end=bar4_start + 0.375)
sax_note10 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375)
sax_note11 = pretty_midi.Note(velocity=100, pitch=40, start=bar4_start + 1.125, end=bar4_start + 1.125 + 0.375)
sax_note12 = pretty_midi.Note(velocity=100, pitch=45, start=bar4_start + 1.5, end=bar4_start + 1.5 + 0.375)
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Bass: Walking line in Fm
bass_notes3 = [
    pretty_midi.Note(velocity=80, pitch=48, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=50, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=47, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=53, start=bar4_start + 1.125, end=bar4_start + 1.5),
    pretty_midi.Note(velocity=80, pitch=50, start=bar4_start + 1.5, end=bar4_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=48, start=bar4_start + 1.875, end=bar4_start + 2.25),
    pretty_midi.Note(velocity=80, pitch=52, start=bar4_start + 2.25, end=bar4_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=53, start=bar4_start + 2.625, end=bar4_start + 3.0)
]
bass.notes.extend(bass_notes3)

# Piano: 7th chords on 2 and 4, F7 on 2, Bb7 on 4
piano_notes3 = [
    # F7 on beat 2 (bar 4)
    pretty_midi.Note(velocity=90, pitch=53, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=52, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=57, start=bar4_start + 0.75, end=bar4_start + 1.125),
    
    # Bb7 on beat 4 (bar 4)
    pretty_midi.Note(velocity=90, pitch=52, start=bar4_start + 1.5, end=bar4_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=49, start=bar4_start + 1.5, end=bar4_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 1.5, end=bar4_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=bar4_start + 1.5, end=bar4_start + 1.875)
]
piano.notes.extend(piano_notes3)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar4_start, end=bar4_end)
drums.notes.extend([kick4, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
