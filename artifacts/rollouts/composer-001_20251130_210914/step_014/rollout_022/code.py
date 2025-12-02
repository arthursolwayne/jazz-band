
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

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + i*0.375, end=bar1_start + i*0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2: Everyone in (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start, end=bar2_start + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start + 1.125, end=bar2_start + 1.5),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=bar2_start + 1.875, end=bar2_start + 2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 2.25, end=bar2_start + 2.625), # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start + 2.625, end=bar2_start + 3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
# D7 on beat 2 (1.5 + 0.75 = 2.25)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F# (7th)
    
    # D7 on beat 4 (1.5 + 1.875 = 3.375) but only within bar 2 (1.5-3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # F# (7th)
]
piano.notes.extend(piano_notes)

# Sax: motif starting on 1
# Motif: D - E - Bb - D (with some space)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=bar2_start + 1.5, end=bar2_start + 1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=bar2_start + 2.25, end=bar2_start + 2.625),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Drums: same pattern
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)

snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.0)

hihat_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=bar3_start + i*0.375, end=bar3_start + i*0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar3_start + 0.75, end=bar3_start + 1.125),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 1.125, end=bar3_start + 1.5),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=bar3_start + 1.5, end=bar3_start + 1.875),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=bar3_start + 1.875, end=bar3_start + 2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar3_start + 2.25, end=bar3_start + 2.625), # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 2.625, end=bar3_start + 3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# D7 on beat 2 (3.0 + 0.75 = 3.75)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F# (7th)
    
    # D7 on beat 4 (3.0 + 1.875 = 4.875) but only within bar 3 (3.0-4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),  # F# (7th)
]
piano.notes.extend(piano_notes)

# Sax: motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=bar3_start + 1.5, end=bar3_start + 1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=bar3_start + 2.25, end=bar3_start + 2.625),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Drums: same pattern
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)

snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)

hihat_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=bar4_start + i*0.375, end=bar4_start + i*0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start, end=bar4_start + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar4_start + 0.75, end=bar4_start + 1.125),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 1.125, end=bar4_start + 1.5),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=bar4_start + 1.5, end=bar4_start + 1.875),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=bar4_start + 1.875, end=bar4_start + 2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=bar4_start + 2.25, end=bar4_start + 2.625), # C
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 2.625, end=bar4_start + 3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# D7 on beat 2 (4.5 + 0.75 = 5.25)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # F# (7th)
    
    # D7 on beat 4 (4.5 + 1.875 = 6.375) but only within bar 4 (4.5-6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),  # F# (7th)
]
piano.notes.extend(piano_notes)

# Sax: motif continuation and resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=bar4_start + 1.5, end=bar4_start + 1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=bar4_start + 2.25, end=bar4_start + 2.625),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=bar4_start + 3.0, end=bar4_start + 3.375),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
