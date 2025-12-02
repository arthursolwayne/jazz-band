
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Map drum notes for Little Ray
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5

# Kick on beats 1 and 3
kick_beats = [bar1_start + 0.375, bar1_start + 1.125]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Snare on beats 2 and 4
snare_beats = [bar1_start + 0.75, bar1_start + 1.5]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_beats = [bar1_start + i * 0.375 for i in range(4)]
for beat in hihat_beats:
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=beat, end=beat + 0.05)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Bass: Marcus - walking line, chromatic approach to Fm
# Fm7 = F, Ab, C, Eb
# Walk down from Bb to F, hit the root on beat 4

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + 1.875, end=bar2_start + 2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start + 2.25, end=bar2_start + 2.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start + 2.625, end=bar2_start + 3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb (root, 3rd, 5th, 7th)
# Chord on beat 2 and beat 4

# Chord on beat 2 (0.75s into bar 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=bar2_start + 0.75, end=bar2_start + 1.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=bar2_start + 0.75, end=bar2_start + 1.125),  # Ab
]

# Chord on beat 4 (1.5s into bar 2)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=bar2_start + 1.5, end=bar2_start + 1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + 1.5, end=bar2_start + 1.875),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=bar2_start + 1.5, end=bar2_start + 1.875),  # Ab
])
piano.notes.extend(piano_notes)

# Drums: continue as in Bar 1
# Kick on 1 and 3
kick_beats = [bar2_start + 0.375, bar2_start + 1.125]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_beats = [bar2_start + 0.75, bar2_start + 1.5]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_beats = [bar2_start + i * 0.375 for i in range(4)]
for beat in hihat_beats:
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=beat, end=beat + 0.05)
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Sax: Dante - short motif, make it sing
# Motif: F (65), Ab (63), C (60), and then leave it hanging — repeat the motif at the end

motif_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=bar3_start + 0.375, end=bar3_start + 0.75),  # F
    pretty_midi.Note(velocity=105, pitch=63, start=bar3_start + 0.75, end=bar3_start + 1.125),  # Ab
    pretty_midi.Note(velocity=105, pitch=60, start=bar3_start + 1.125, end=bar3_start + 1.5),  # C
    # Leave it hanging — repeat at the end of the bar
    pretty_midi.Note(velocity=105, pitch=65, start=bar3_start + 3.0, end=bar3_start + 3.375),  # F
    pretty_midi.Note(velocity=105, pitch=63, start=bar3_start + 3.375, end=bar3_start + 3.75),  # Ab
    pretty_midi.Note(velocity=105, pitch=60, start=bar3_start + 3.75, end=bar3_start + 4.125),  # C
]
sax.notes.extend(motif_notes)

# Bass: Marcus - walking line again, chromatic approach

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=bar3_start + 0.375, end=bar3_start + 0.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=bar3_start + 0.75, end=bar3_start + 1.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 1.125, end=bar3_start + 1.5),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar3_start + 1.5, end=bar3_start + 1.875),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=bar3_start + 1.875, end=bar3_start + 2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=bar3_start + 2.25, end=bar3_start + 2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=bar3_start + 2.625, end=bar3_start + 3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Diane - comp on 2 and 4 again, same as bar 2

piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=bar3_start + 0.75, end=bar3_start + 1.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=bar3_start + 0.75, end=bar3_start + 1.125),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=bar3_start + 0.75, end=bar3_start + 1.125),  # Ab
]

# Chord on beat 4 (1.5s into bar 3)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 1.5, end=bar3_start + 1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=bar3_start + 1.5, end=bar3_start + 1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=bar3_start + 1.5, end=bar3_start + 1.875),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=bar3_start + 1.5, end=bar3_start + 1.875),  # Ab
])
piano.notes.extend(piano_notes)

# Drums: continue the pattern

# Kick on 1 and 3
kick_beats = [bar3_start + 0.375, bar3_start + 1.125]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_beats = [bar3_start + 0.75, bar3_start + 1.5]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_beats = [bar3_start + i * 0.375 for i in range(4)]
for beat in hihat_beats:
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=beat, end=beat + 0.05)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Sax: Dante - repeat the motif, complete the phrase

motif_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=bar4_start + 0.375, end=bar4_start + 0.75),  # F
    pretty_midi.Note(velocity=105, pitch=63, start=bar4_start + 0.75, end=bar4_start + 1.125),  # Ab
    pretty_midi.Note(velocity=105, pitch=60, start=bar4_start + 1.125, end=bar4_start + 1.5),  # C
    pretty_midi.Note(velocity=105, pitch=65, start=bar4_start + 1.5, end=bar4_start + 1.875),  # F
    pretty_midi.Note(velocity=105, pitch=63, start=bar4_start + 1.875, end=bar4_start + 2.25),  # Ab
    pretty_midi.Note(velocity=105, pitch=60, start=bar4_start + 2.25, end=bar4_start + 2.625),  # C
    pretty_midi.Note(velocity=105, pitch=65, start=bar4_start + 2.625, end=bar4_start + 3.0),  # F
]
sax.notes.extend(motif_notes)

# Bass: Marcus - walking line again, closing the phrase

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=bar4_start + 0.375, end=bar4_start + 0.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=bar4_start + 0.75, end=bar4_start + 1.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start + 1.125, end=bar4_start + 1.5),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar4_start + 1.5, end=bar4_start + 1.875),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=bar4_start + 1.875, end=bar4_start + 2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=bar4_start + 2.25, end=bar4_start + 2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=bar4_start + 2.625, end=bar4_start + 3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - hold the last chord, don’t comp

# Hold Fm7 for the remainder of the bar
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=bar4_start + 0.0, end=bar4_end),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=bar4_start + 0.0, end=bar4_end),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=bar4_start + 0.0, end=bar4_end),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=bar4_start + 0.0, end=bar4_end),  # Ab
]
piano.notes.extend(piano_notes)

# Drums: continue the pattern

# Kick on 1 and 3
kick_beats = [bar4_start + 0.375, bar4_start + 1.125]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_beats = [bar4_start + 0.75, bar4_start + 1.5]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=beat, end=beat + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_beats = [bar4_start + i * 0.375 for i in range(4)]
for beat in hihat_beats:
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=beat, end=beat + 0.05)
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
