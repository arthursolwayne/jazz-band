
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar: 1.5 seconds (160 BPM, 4/4 time)
BAR_DURATION = 1.5
BAR_1_START = 0.0
BAR_1_END = BAR_DURATION
BAR_2_START = BAR_1_END
BAR_4_END = BAR_1_END * 3  # 4 bars total

# ----------------------------
# BAR 1: DRUMS ONLY
# Little Ray sets the mood with space and rhythm
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Build tension with subtle fills and space

# Time signatures
# Bar 1: 0.0 - 1.5s
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=80, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=80, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(velocity=60, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

# ----------------------------
# BAR 2-4: FULL QUARTET
# Bar 2: 1.5 - 3.0s

# SAX: Tenor motif in F minor (F, Ab, Bb, D)
# Phrase: F Ab Bb D (1.5 - 2.0s)
# Leave it hanging (2.0 - 2.5s)
# Then come back (2.5 - 3.0s) with resolution

note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)  # F
note2 = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5)  # Ab
note3 = pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.0)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5)  # D
sax.notes.extend([note1, note2, note3, note4])

# BASS: Walking bass line with chromatic motion
# F -> Eb -> D -> C -> B -> Bb -> A -> Ab -> G -> F (chromatic descent)
# 1.5s to 3.0s

# F (1.5s)
note = pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75)
bass.notes.append(note)
# Eb (1.75s)
note = pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0)
bass.notes.append(note)
# D (2.0s)
note = pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25)
bass.notes.append(note)
# C (2.25s)
note = pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5)
bass.notes.append(note)
# B (2.5s)
note = pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=2.75)
bass.notes.append(note)
# Bb (2.75s)
note = pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0)
bass.notes.append(note)

# PIANO: 7th chords, comp on offbeats, angry but supporting
# F7 on 1 (1.5s), Bb7 on 2 (2.0s), Ab7 on 3 (2.5s), D7 on 4 (3.0s)

# F7 = F, A, C, Eb
note = pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=70, pitch=68, start=1.5, end=1.75)
note3 = pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.75)
note4 = pretty_midi.Note(velocity=70, pitch=64, start=1.5, end=1.75)
piano.notes.extend([note, note2, note3, note4])

# Bb7 on 2 (2.0s)
note = pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25)
note2 = pretty_midi.Note(velocity=70, pitch=66, start=2.0, end=2.25)
note3 = pretty_midi.Note(velocity=70, pitch=62, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=70, pitch=60, start=2.0, end=2.25)
piano.notes.extend([note, note2, note3, note4])

# Ab7 on 3 (2.5s)
note = pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75)
note2 = pretty_midi.Note(velocity=70, pitch=64, start=2.5, end=2.75)
note3 = pretty_midi.Note(velocity=70, pitch=60, start=2.5, end=2.75)
note4 = pretty_midi.Note(velocity=70, pitch=59, start=2.5, end=2.75)
piano.notes.extend([note, note2, note3, note4])

# D7 on 4 (3.0s)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25)
note2 = pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.25)
note3 = pretty_midi.Note(velocity=70, pitch=59, start=3.0, end=3.25)
note4 = pretty_midi.Note(velocity=70, pitch=57, start=3.0, end=3.25)
piano.notes.extend([note, note2, note3, note4])

# DRUMS: Continue with the same pattern for bars 2 and 3
# Bar 2: 1.5 - 3.0s

for i in range(4):
    time = 1.5 + i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=80, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=80, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(velocity=60, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5s (not shown, but pattern repeats)
# Bar 4: 4.5 - 6.0s (end of piece, same pattern)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro_in_F.mid")
