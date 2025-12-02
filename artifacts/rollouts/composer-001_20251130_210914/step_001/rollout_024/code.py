
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
bar1_duration = 1.5
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start, end=bar1_start + bar1_duration, step=0.375)

for i in range(int(bar1_duration / 0.375)):
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat_note)

drums.notes.append(kick)
drums.notes.append(snare)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=bar2_start, end=bar2_start + 0.375),    # D
    pretty_midi.Note(velocity=100, pitch=51, start=bar2_start + 0.375, end=bar2_start + 0.75), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=bar2_start + 0.75, end=bar2_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=49, start=bar2_start + 1.125, end=bar2_start + 1.5), # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar2_start + 0.75, end=bar2_start + 1.125), # B
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 0.75, end=bar2_start + 1.125), # F
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start + 1.125, end=bar2_start + 1.5), # E
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.125, end=bar2_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=68, start=bar2_start + 1.125, end=bar2_start + 1.5), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 1.125, end=bar2_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar2_start, end=bar2_start + bar1_duration, step=0.375)

for i in range(int(bar1_duration / 0.375)):
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat_note)

drums.notes.append(kick)
drums.notes.append(snare)

# Sax: motif starting on Dm7, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=66, start=bar2_start + 0.375, end=bar2_start + 0.75), # G
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 0.75, end=bar2_start + 1.125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.125, end=bar2_start + 1.5), # Gb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=bar3_start, end=bar3_start + 0.375),    # D
    pretty_midi.Note(velocity=100, pitch=51, start=bar3_start + 0.375, end=bar3_start + 0.75), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=bar3_start + 0.75, end=bar3_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=49, start=bar3_start + 1.125, end=bar3_start + 1.5), # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar3_start + 0.75, end=bar3_start + 1.125), # B
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar3_start + 0.75, end=bar3_start + 1.125), # F
    pretty_midi.Note(velocity=100, pitch=74, start=bar3_start + 1.125, end=bar3_start + 1.5), # E
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 1.125, end=bar3_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=68, start=bar3_start + 1.125, end=bar3_start + 1.5), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 1.125, end=bar3_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar3_start, end=bar3_start + bar1_duration, step=0.375)

for i in range(int(bar1_duration / 0.375)):
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat_note)

drums.notes.append(kick)
drums.notes.append(snare)

# Sax: motif continuation, resolving the tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start, end=bar3_start + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=66, start=bar3_start + 0.375, end=bar3_start + 0.75), # G
    pretty_midi.Note(velocity=100, pitch=60, start=bar3_start + 0.75, end=bar3_start + 1.125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + 1.125, end=bar3_start + 1.5), # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=bar4_start, end=bar4_start + 0.375),    # D
    pretty_midi.Note(velocity=100, pitch=51, start=bar4_start + 0.375, end=bar4_start + 0.75), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=bar4_start + 0.75, end=bar4_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=49, start=bar4_start + 1.125, end=bar4_start + 1.5), # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar4_start + 0.75, end=bar4_start + 1.125), # B
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar4_start + 0.75, end=bar4_start + 1.125), # F
    pretty_midi.Note(velocity=100, pitch=74, start=bar4_start + 1.125, end=bar4_start + 1.5), # E
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=68, start=bar4_start + 1.125, end=bar4_start + 1.5), # G
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 1.125, end=bar4_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=bar4_start, end=bar4_start + bar1_duration, step=0.375)

for i in range(int(bar1_duration / 0.375)):
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat_note)

drums.notes.append(kick)
drums.notes.append(snare)

# Sax: motif resolution, holding the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start, end=bar4_start + 0.375), # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 0.375, end=bar4_start + 0.75), # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 0.75, end=bar4_start + 1.125), # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 1.125, end=bar4_start + 1.5), # Gb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
