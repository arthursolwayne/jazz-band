
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 60 BPM = 1 beat = 0.375s → 1 bar = 1.5s

for bar in [0]:  # Bar 1
    start = bar * 1.5
    # Kick on 1 and 3
    kick_times = [start + 0.0, start + 0.75]
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.25)
        drums.notes.append(note)
    
    # Snare on 2 and 4
    snare_times = [start + 0.375, start + 1.125]
    for time in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.25)
        drums.notes.append(note)
    
    # Hihat on every eighth
    hihat_times = [start + t * 0.375 for t in range(0, 8)]
    for time in hihat_times:
        note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Time signature: 4/4, so each bar is 1.5s
# Bar 2: Start of the sax melody (Dm7 in D minor)
# Your motif: Dm7 -> Eb7 -> Fm7 -> G7
# Keep the motif short, singable, and suggestive.

# Dm7: D, F, A, C
# Eb7: Eb, G, Bb, Db
# Fm7: F, Ab, C, Eb
# G7: G, B, D, F

# Bar 2 (1.5s)
# Start with Dm7 chord, but play only the D and F (Dorian minor)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75)  # F
sax.notes.append(note)

# Bar 3 (3.0s)
# Move to Eb7, play only Eb and G
note = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125)  # Eb
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25)  # G
sax.notes.append(note)

# Bar 4 (4.5s)
# Move to Fm7, play only F and Ab
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=4.625, end=4.75)  # Ab
sax.notes.append(note)

# Bass: Walking line in Dm -> Eb7 -> Fm7 -> G7
# Dm: D, C, Bb, A, G, F, Eb, D
# Eb7: Eb, D, C, Bb, A, G, F, Eb
# Fm7: F, Eb, D, C, Bb, A, G, F
# G7: G, F, Eb, D, C, Bb, A, G

for bar in [1, 2, 3]:  # Bars 2-4
    start = bar * 1.5
    # Walking line: 8th notes, chromatic, never the same note twice
    if bar == 1:
        # Dm -> Eb7
        notes = [62, 60, 59, 58, 60, 59, 58, 57]  # D, C, Bb, A, G, F, Eb, D
    elif bar == 2:
        # Eb7 -> Fm7
        notes = [66, 65, 64, 62, 64, 62, 60, 59]  # Eb, D, C, Bb, A, G, F, Eb
    elif bar == 3:
        # Fm7 -> G7
        notes = [67, 65, 64, 62, 64, 62, 60, 59]  # F, Eb, D, C, Bb, A, G, F

    # Play walking line
    for i, pitch in enumerate(notes):
        time = start + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
        bass.notes.append(note)

# Piano: 7th chords on 2 and 4
for bar in [1, 2, 3]:  # Bars 2-4
    start = bar * 1.5
    if bar == 1:
        # Dm7 on beat 2 and 4
        chord = [62, 65, 67, 69]  # D, F, A, C
        for i in [1, 3]:
            time = start + i * 0.375
            for pitch in chord:
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)
    elif bar == 2:
        # Eb7 on beat 2 and 4
        chord = [66, 69, 71, 73]  # Eb, G, Bb, Db
        for i in [1, 3]:
            time = start + i * 0.375
            for pitch in chord:
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)
    elif bar == 3:
        # Fm7 on beat 2 and 4
        chord = [67, 70, 72, 74]  # F, Ab, C, Eb
        for i in [1, 3]:
            time = start + i * 0.375
            for pitch in chord:
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)

# Drums: Continue for bars 2-4
for bar in [1, 2, 3]:  # Bars 2-4
    start = bar * 1.5
    # Kick on 1 and 3
    kick_times = [start + 0.0, start + 0.75]
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.25)
        drums.notes.append(note)
    
    # Snare on 2 and 4
    snare_times = [start + 0.375, start + 1.125]
    for time in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.25)
        drums.notes.append(note)
    
    # Hihat on every eighth
    hihat_times = [start + t * 0.375 for t in range(0, 8)]
    for time in hihat_times:
        note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_russo_intro.mid")
