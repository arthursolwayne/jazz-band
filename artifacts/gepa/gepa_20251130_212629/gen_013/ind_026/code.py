
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Acoustic Bass
piano = pretty_midi.Instrument(program=0)      # Electric Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Time per bar at 160 BPM: 1.5 seconds
bar_length = 1.5

# BAR 1: Little Ray (drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42, 42, 42, 42]  # 4 eighth notes

kick_times = [0.0, bar_length / 2.0]
snare_times = [bar_length / 4.0, bar_length * 3 / 4.0]
hihat_times = [bar_length * i / 4.0 for i in range(4)]

for note, time in zip(kick_notes, kick_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# BAR 2-4: Full quartet (1.5 - 6.0s)
# Time starts at 1.5 seconds

# BASS LINE: Marcus (Walking line in Dm, chromatic approaches)
# Dm chord: D F A C (Dm7 = D F A C)
# Bass line in Dm: D F Ab C (Ab is chromatic approach to G, leading to C)
# Bar 2: D -> F -> Ab -> C
# Bar 3: C -> B -> A -> G (chromatic approach down)
# Bar 4: G -> F -> D -> D (resolve)

bass_notes = [
    62,  # D
    64,  # F
    60,  # Ab
    67,  # C

    67,  # C
    66,  # B
    65,  # A
    64,  # G

    64,  # G
    62,  # F
    62,  # D
    62   # D
]

bass_times = [1.5 + bar_length * i / 4.0 for i in range(12)]

for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# PIANO: Diane (7th chords, comp on 2 and 4)
# Dm7 = D F A C
# Dm7 = D F A C (spelled out as 7th chord)
# Comp on 2 and 4

# Bar 2: Dm7 on 2nd beat
# Bar 3: Dm7 on 2nd beat
# Bar 4: Dm7 on 2nd beat

piano_notes = [
    # Bar 2: Dm7 on beat 2
    62, 64, 67, 60,  # D F A C
    # Bar 3: Dm7 on beat 2
    62, 64, 67, 60,
    # Bar 4: Dm7 on beat 2
    62, 64, 67, 60
]

piano_times = [
    1.5 + bar_length / 4.0,  # Beat 2 of bar 2
    1.5 + bar_length / 4.0 + 0.25,  # D
    1.5 + bar_length / 4.0 + 0.5,  # F
    1.5 + bar_length / 4.0 + 0.75,  # A
    1.5 + bar_length / 4.0 + 1.0,  # C

    1.5 + bar_length * 2 / 4.0,  # Beat 2 of bar 3
    1.5 + bar_length * 2 / 4.0 + 0.25,
    1.5 + bar_length * 2 / 4.0 + 0.5,
    1.5 + bar_length * 2 / 4.0 + 0.75,
    1.5 + bar_length * 2 / 4.0 + 1.0,

    1.5 + bar_length * 3 / 4.0,  # Beat 2 of bar 4
    1.5 + bar_length * 3 / 4.0 + 0.25,
    1.5 + bar_length * 3 / 4.0 + 0.5,
    1.5 + bar_length * 3 / 4.0 + 0.75,
    1.5 + bar_length * 3 / 4.0 + 1.0,
]

for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# SAX: Dante (your motif)
# Motif: D (62) -> F (64) -> Ab (60) -> C (67), with a question mark
# D -> F -> Ab -> C (the root, 3rd, b7, 7th of Dm7)
# Play the first three notes (D, F, Ab) and leave the C hanging
# Then come back in bar 4 to resolve on C

sax_notes = [
    62,  # D
    64,  # F
    60,  # Ab
    67,  # C
]

sax_times = [
    1.5 + 0.25,  # D on beat 1
    1.5 + 0.5,   # F on beat 2
    1.5 + 0.75,  # Ab on beat 3
    1.5 + 1.0,   # C on beat 4 (Bar 2)
]

# Repeat in bar 3 with same rhythm
sax_notes.extend([
    62,  # D
    64,  # F
    60,  # Ab
    67,  # C
])

sax_times.extend([
    1.5 + bar_length + 0.25,
    1.5 + bar_length + 0.5,
    1.5 + bar_length + 0.75,
    1.5 + bar_length + 1.0
])

# In bar 4, resolve to C
sax_notes.extend([
    67,  # C on beat 2
])

sax_times.extend([
    1.5 + bar_length * 2 + 0.5
])

for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
