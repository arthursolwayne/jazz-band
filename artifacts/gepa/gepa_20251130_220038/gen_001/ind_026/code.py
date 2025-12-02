
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
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar1_start, end=bar1_end, step=0.375)
drums.notes.extend([kick, snare])
for i in range(4):
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.375)
    drums.notes.append(hihat_note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass: Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + 0.375, end=bar2_start + 0.75), # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start + 0.75, end=bar2_start + 1.125), # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start + 1.125, end=bar2_start + 1.5), # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 1.125, end=bar2_start + 1.5), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 1.125, end=bar2_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.125, end=bar2_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif starts here
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start, end=bar2_start + 0.375), # E
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75), # G
    pretty_midi.Note(velocity=110, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125), # F
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start + 1.125, end=bar2_start + 1.5), # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 1.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar3_start, end=bar3_end, step=0.375)
drums.notes.extend([kick, snare])
for i in range(4):
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.375)
    drums.notes.append(hihat_note)

# Bass: Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=bar3_start, end=bar3_start + 0.375),   # E
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 0.375, end=bar3_start + 0.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar3_start + 0.75, end=bar3_start + 1.125), # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 1.125, end=bar3_start + 1.5), # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 1.125, end=bar3_start + 1.5), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 1.125, end=bar3_start + 1.5), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar3_start + 1.125, end=bar3_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 1.125, end=bar3_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=bar3_start, end=bar3_start + 0.375), # G
    pretty_midi.Note(velocity=110, pitch=64, start=bar3_start + 0.375, end=bar3_start + 0.75), # F
    pretty_midi.Note(velocity=110, pitch=65, start=bar3_start + 0.75, end=bar3_start + 1.125), # E
    pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 1.125, end=bar3_start + 1.5), # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 1.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar4_start, end=bar4_end, step=0.375)
drums.notes.extend([kick, snare])
for i in range(4):
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    drums.notes.append(hihat_note)

# Bass: Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=bar4_start, end=bar4_start + 0.375),   # E
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start + 0.375, end=bar4_start + 0.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar4_start + 0.75, end=bar4_start + 1.125), # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start + 1.125, end=bar4_start + 1.5), # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 1.125, end=bar4_start + 1.5), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 1.125, end=bar4_start + 1.5), # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5), # C
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5), # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=bar4_start, end=bar4_start + 0.375), # F
    pretty_midi.Note(velocity=110, pitch=65, start=bar4_start + 0.375, end=bar4_start + 0.75), # E
    pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125), # G
    pretty_midi.Note(velocity=110, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5), # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
