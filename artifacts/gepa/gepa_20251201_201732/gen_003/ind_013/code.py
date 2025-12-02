
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: F major (no sharps or flats)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0, 0)]  # F major, no mode change

# Define time in seconds per bar (160 BPM, 4/4)
time_per_bar = 60.0 / 160 * 4  # 6 seconds per 4 bars

# Define the note duration in seconds (quarter note = 0.375s at 160 BPM)
note_duration = 0.375

# Define instruments
# Tenor sax (program 64)
tenor_sax = pretty_midi.Instrument(program=64)

# Bass (program 33)
bass = pretty_midi.Instrument(program=33)

# Piano (program 0)
piano = pretty_midi.Instrument(program=0)

# Drums (program 11)
drums = pretty_midi.Instrument(program=11)

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    # Time for Bar 1
    start_time = bar * time_per_bar

    # Kick
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + note_duration)
    drums.notes.append(kick_note)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=start_time + note_duration * 2, end=start_time + note_duration * 3)
    drums.notes.append(kick_note)

    # Snare
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=start_time + note_duration, end=start_time + note_duration * 2)
    drums.notes.append(snare_note)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=start_time + note_duration * 3, end=start_time + note_duration * 4)
    drums.notes.append(snare_note)

    # Hihat
    for i in range(8):
        hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * note_duration / 2, end=start_time + i * note_duration / 2 + 0.05)
        drums.notes.append(hihat_note)

# Bar 2: Everyone in
# Bass: Walking line in F major (D2-G2, roots and fifths with chromatic approaches)
# Bar 2: F7 (F A C E), root (F), fifth (C), chromatic approach (E)
bass_note1 = pretty_midi.Note(velocity=80, pitch=71, start=note_duration * 4, end=note_duration * 5)  # F
bass.notes.append(bass_note1)
bass_note2 = pretty_midi.Note(velocity=80, pitch=69, start=note_duration * 5, end=note_duration * 6)  # E (chromatic approach to F)
bass.notes.append(bass_note2)
bass_note3 = pretty_midi.Note(velocity=80, pitch=71, start=note_duration * 6, end=note_duration * 7)  # F
bass.notes.append(bass_note3)
bass_note4 = pretty_midi.Note(velocity=80, pitch=76, start=note_duration * 7, end=note_duration * 8)  # C
bass.notes.append(bass_note4)

# Piano: Open voicing, F7 (F A C E), resolve on the last chord
# Bar 2: F7
piano_note1 = pretty_midi.Note(velocity=100, pitch=71, start=note_duration * 4, end=note_duration * 5)  # F
piano_note2 = pretty_midi.Note(velocity=100, pitch=76, start=note_duration * 4, end=note_duration * 5)  # C
piano_note3 = pretty_midi.Note(velocity=100, pitch=78, start=note_duration * 4, end=note_duration * 5)  # E
piano_note4 = pretty_midi.Note(velocity=100, pitch=81, start=note_duration * 4, end=note_duration * 5)  # A
piano.notes.append(piano_note1)
piano.notes.append(piano_note2)
piano.notes.append(piano_note3)
piano.notes.append(piano_note4)

# Bar 3: Bb7 (Bb D F A), open voicing
piano_note1 = pretty_midi.Note(velocity=100, pitch=67, start=note_duration * 5, end=note_duration * 6)  # Bb
piano_note2 = pretty_midi.Note(velocity=100, pitch=72, start=note_duration * 5, end=note_duration * 6)  # D
piano_note3 = pretty_midi.Note(velocity=100, pitch=74, start=note_duration * 5, end=note_duration * 6)  # F
piano_note4 = pretty_midi.Note(velocity=100, pitch=77, start=note_duration * 5, end=note_duration * 6)  # A
piano.notes.append(piano_note1)
piano.notes.append(piano_note2)
piano.notes.append(piano_note3)
piano.notes.append(piano_note4)

# Bar 4: C7 (C E G B), resolve
piano_note1 = pretty_midi.Note(velocity=100, pitch=60, start=note_duration * 6, end=note_duration * 7)  # C
piano_note2 = pretty_midi.Note(velocity=100, pitch=64, start=note_duration * 6, end=note_duration * 7)  # E
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=note_duration * 6, end=note_duration * 7)  # G
piano_note4 = pretty_midi.Note(velocity=100, pitch=71, start=note_duration * 6, end=note_duration * 7)  # B
piano.notes.append(piano_note1)
piano.notes.append(piano_note2)
piano.notes.append(piano_note3)
piano.notes.append(piano_note4)

# Tenor sax: One short motif, starting on F, resolving on the 4th bar with a rest in between
# Bar 2: F
sax_note1 = pretty_midi.Note(velocity=100, pitch=71, start=note_duration * 4, end=note_duration * 5)
tenor_sax.notes.append(sax_note1)

# Bar 3: Bb (rest in first half, play in second half)
sax_note2 = pretty_midi.Note(velocity=100, pitch=67, start=note_duration * 6, end=note_duration * 7)
tenor_sax.notes.append(sax_note2)

# Bar 4: C (rest in first half, play in second half)
sax_note3 = pretty_midi.Note(velocity=100, pitch=60, start=note_duration * 7, end=note_duration * 8)
tenor_sax.notes.append(sax_note3)

# Add instruments to the PrettyMIDI object
pm.instruments = [tenor_sax, bass, piano, drums]

# Save the MIDI file
pm.write("wayne_intro.mid")
