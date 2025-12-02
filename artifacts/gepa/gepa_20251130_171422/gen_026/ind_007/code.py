
import pretty_midi

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
Fm = pretty_midi.PitchClassSet([7, 8, 10, 11, 12, 14, 16])  # F, Gb, Ab, Bb, B, Db, Eb

# Drums (Little Ray)
drums = pretty_midi.Instrument(program=10)

# Tenor sax (you)
tenor_sax = pretty_midi.Instrument(program=64)

# Bass (Marcus)
bass = pretty_midi.Instrument(program=33)

# Piano (Diane)
piano = pretty_midi.Instrument(program=0)

# Add instruments to the MIDI file
pm.instruments = [drums, tenor_sax, bass, piano]

# Time per bar at 160 BPM
# 60 seconds / 160 BPM = 0.375 seconds per beat
# 4 bars * 4 beats = 16 beats = 6 seconds
# Each beat is 0.375 seconds, each bar is 1.5 seconds

# Bar 1: Drums only
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
for beat in range(4):
    # Kick on 1 and 3
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hi-hat on every eighth
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(beat * 0.375) + (eighth * 0.1875), end=(beat * 0.375) + (eighth * 0.1875) + 0.05)
        drums.notes.append(note)

# Bar 2: Bass, Piano, Tenor
# Tenor sax motif: F (7), Bb (11), B (12), Ab (10)
# Start on beat 1, end on beat 4 — leave it hanging on beat 3
note = pretty_midi.Note(velocity=100, pitch=7, start=1.5, end=1.6)
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=11, start=1.6, end=1.7)
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=12, start=1.7, end=1.8)
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=10, start=1.8, end=1.9)
tenor_sax.notes.append(note)

# Bass line: F (7), Gb (8), Ab (10), Bb (11), B (12), Db (14), Eb (16)
# Walking line with chromatic approach on beat 3
bass_line = [7, 8, 10, 11, 12, 14, 16, 11]
for i, pitch in enumerate(bass_line):
    start = 1.5 + i * 0.375
    end = start + 0.25
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords, comping on 2 and 4
# F7 (7, 11, 12, 15)
# Ab7 (10, 14, 15, 18)
# Bb7 (11, 14, 16, 19)
for bar in range(2, 4):
    time = bar * 1.5
    if bar % 2 == 0:  # 2nd bar
        # F7
        for pitch in [7, 11, 12, 15]:
            note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
            piano.notes.append(note)
    else:  # 3rd bar
        # Ab7
        for pitch in [10, 14, 15, 18]:
            note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
            piano.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")

print("Intro MIDI saved as 'dante_russo_intro.mid'")
