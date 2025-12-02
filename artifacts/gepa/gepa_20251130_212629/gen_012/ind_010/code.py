
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
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i*0.375, end=bar1_start + i*0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Bass line: walking line in Dm, chromatic approaches
# Dm7: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 1.125, end=bar2_start + 1.5),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 1.5, end=bar2_start + 1.875),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=bar2_start + 1.875, end=bar2_start + 2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=bar2_start + 2.25, end=bar2_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 2.625, end=bar2_start + 3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7: D F A C (1st beat), then rest on 2, comp on 2 and 4
piano_notes = [
    # Dm7 on beat 1
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start, end=bar2_start + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start, end=bar2_start + 0.375),  # C
    # Comp on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 0.75, end=bar2_start + 0.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.75, end=bar2_start + 0.875),  # C
    # Comp on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 2.625, end=bar2_start + 2.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 2.625, end=bar2_start + 2.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 2.625, end=bar2_start + 2.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: short motif starting on beat 1, leaving it hanging, then returning
# Dm: D F A C
# Motif: D -> F -> A -> rest, then D -> F -> A -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.375, end=bar2_start + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 2.25, end=bar2_start + 2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 2.625, end=bar2_start + 3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 3.0, end=bar2_start + 3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 3.375, end=bar2_start + 3.75),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Bass line: walking line in Dm, chromatic approaches
# Repeat of bar 2 bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=bar3_start + 1.125, end=bar3_start + 1.5),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 1.5, end=bar3_start + 1.875),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=bar3_start + 1.875, end=bar3_start + 2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=bar3_start + 2.25, end=bar3_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start + 2.625, end=bar3_start + 3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 on beat 1, rest on 2, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=bar3_start, end=bar3_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start, end=bar3_start + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start, end=bar3_start + 0.375),  # C
    # Comp on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.75, end=bar3_start + 0.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 0.75, end=bar3_start + 0.875),  # C
    # Comp on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=bar3_start + 2.625, end=bar3_start + 2.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start + 2.625, end=bar3_start + 2.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 2.625, end=bar3_start + 2.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif, completing the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 3.375, end=bar3_start + 3.75),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + i*0.375, end=bar4_start + i*0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bass line: walking line in Dm, chromatic approaches
# Dm7: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=bar4_start + 1.125, end=bar4_start + 1.5),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 1.5, end=bar4_start + 1.875),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=bar4_start + 1.875, end=bar4_start + 2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=bar4_start + 2.25, end=bar4_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 2.625, end=bar4_start + 3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 on beat 1, rest on 2, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start, end=bar4_start + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start, end=bar4_start + 0.375),  # C
    # Comp on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 0.75, end=bar4_start + 0.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 0.75, end=bar4_start + 0.875),  # C
    # Comp on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=bar4_start + 2.625, end=bar4_start + 2.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 2.625, end=bar4_start + 2.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 2.625, end=bar4_start + 2.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif, completing the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar4_start + 1.5, end=bar4_start + 1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 1.875, end=bar4_start + 2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 2.25, end=bar4_start + 2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 2.625, end=bar4_start + 3.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
