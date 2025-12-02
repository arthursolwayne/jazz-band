
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define instruments
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0)      # Drums (use percussion instruments)

pm.instruments = [tenor_sax, bass, piano, drums]

# BPM = 160
# 4/4 time
# 6 seconds for 4 bars
# Each bar = 1.5 seconds
# Each beat = 0.375 seconds

# Define time stamps based on 160 BPM
# Note: 60 / 160 = 0.375 seconds per beat

# --- DRUMS: Little Ray (Bar 1) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
bar1_start = 0.0
bar1_end = 1.5

# Kick on beats 1 and 3
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(
        velocity=90,
        pitch=36,  # Kick drum
        start=t,
        end=t + 0.2
    )
    drums.notes.append(note)

# Snare on beats 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(
        velocity=95,
        pitch=38,  # Snare drum
        start=t,
        end=t + 0.15
    )
    drums.notes.append(note)

# Hi-hat on every 8th note
hihat_times = [bar1_start + t * 0.375 for t in range(0, 8)]
for t in hihat_times:
    note = pretty_midi.Note(
        velocity=70,
        pitch=42,  # Hi-hat
        start=t,
        end=t + 0.1
    )
    drums.notes.append(note)

# --- BASS: Marcus (Bars 2-4) ---
# Walking line, chromatic approaches, no repeated notes
# F major key
# F, G, A, Bb, C, D, E, F...

# Bass line (F, G, A, Bb, C, D, E, F)
bass_notes = [71, 72, 74, 73, 76, 77, 79, 71]
bass_durations = [0.375] * 8

bar2_start = 1.5
for i, note in enumerate(bass_notes):
    start = bar2_start + i * 0.375
    end = start + bass_durations[i]
    note_obj = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=start,
        end=end
    )
    bass.notes.append(note_obj)

# --- PIANO: Diane (Bars 2-4) ---
# 7th chords, comp on 2 and 4
# F7 = F, A, C, E♭
# B7 = B, D#, F#, A
# E7 = E, G#, B, D
# A7 = A, C#, E, G

# Bar 2: F7
bar2_start = 1.5
chord_notes = [71, 74, 76, 70]
for note in chord_notes:
    note_obj = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=bar2_start + 0.75,
        end=bar2_start + 1.125
    )
    piano.notes.append(note_obj)

# Bar 3: B7
bar3_start = 3.0
chord_notes = [77, 81, 83, 87]
for note in chord_notes:
    note_obj = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=bar3_start + 0.75,
        end=bar3_start + 1.125
    )
    piano.notes.append(note_obj)

# Bar 4: E7
bar4_start = 4.5
chord_notes = [76, 80, 83, 79]
for note in chord_notes:
    note_obj = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=bar4_start + 0.75,
        end=bar4_start + 1.125
    )
    piano.notes.append(note_obj)

# --- SAX: You (Bars 2-4) ---
# Sparse, emotive melody: F, Bb, C, F
# Spread across bars 2-3, with a pause in bar 4, ending on a low F

# Bar 2: F (beat 1)
note = pretty_midi.Note(
    velocity=100,
    pitch=71,
    start=bar2_start + 0.0,
    end=bar2_start + 0.375
)
tenor_sax.notes.append(note)

# Bar 2: Bb (beat 3)
note = pretty_midi.Note(
    velocity=95,
    pitch=73,
    start=bar2_start + 0.75,
    end=bar2_start + 1.125
)
tenor_sax.notes.append(note)

# Bar 3: C (beat 2)
note = pretty_midi.Note(
    velocity=105,
    pitch=76,
    start=bar3_start + 0.375,
    end=bar3_start + 0.75
)
tenor_sax.notes.append(note)

# Bar 4: F (beat 3, but lower, with a soft dynamic)
note = pretty_midi.Note(
    velocity=70,
    pitch=63,  # F in the lower register
    start=bar4_start + 0.75,
    end=bar4_start + 1.125
)
tenor_sax.notes.append(note)

# Write to MIDI file
pm.write("wayne_intro.mid")
print("MIDI file written to 'wayne_intro.mid'")
