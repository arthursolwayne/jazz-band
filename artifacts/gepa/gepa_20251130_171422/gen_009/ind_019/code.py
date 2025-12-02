
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: F Major
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major (key number 5)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drum kit
bass = pretty_midi.Instrument(program=33)   # Double bass
piano = pretty_midi.NotesInstrument(program=0)  # Acoustic piano
sax = pretty_midi.Instrument(program=64)    # Tenor saxophone

pm.instruments = [drums, bass, piano, sax]

#---------------------
# BAR 1: DRUMS ONLY
#---------------------

# Timing: 4/4, 160 BPM
# Bar length = 6 seconds / 4 = 1.5 seconds per bar
# Beat = 0.375s
# Note durations in beats:

# Kick on 1 and 3
kick_notes = [
    (0.0, 36, 100),  # Kick on beat 0 (1)
    (1.125, 36, 100),  # Kick on beat 3 (1.125)
]

# Snare on 2 and 4
snare_notes = [
    (0.75, 38, 100),  # Snare on beat 2 (0.75)
    (1.5, 38, 100),   # Snare on beat 4 (1.5)
]

# Hi-hat on every 8th note
hihat_notes = [
    (0.0, 42, 100),
    (0.375, 42, 100),
    (0.75, 42, 100),
    (1.125, 42, 100),
    (1.5, 42, 100),
]

# Add to drums instrument
for note in kick_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))
for note in snare_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))
for note in hihat_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

#---------------------
# BAR 2: FULL ENSEMBLE
#---------------------

# BASS LINE: Walking in F major, chromatic approach to Bb
# F -> Bb -> C -> E -> F (chromatic approach on Bb)
# 1st beat: F (1), 2nd beat: Bb (2), 3rd beat: C (3), 4th beat: E (4)

bass_notes = [
    (1.5, 65, 100),  # F (1)
    (1.875, 70, 100), # Bb (2)
    (2.25, 67, 100),  # C (3)
    (2.625, 69, 100), # E (4)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# PIANO: 7th chords, comp on 2 and 4
# F7 on beat 2, F7 again on beat 4

# F7 = F, A, C, Eb
# On beat 2 and 4

piano_notes = [
    # Beat 2 (1.875)
    (1.875, 65, 100),  # F
    (1.875, 68, 100),  # A
    (1.875, 67, 100),  # C
    (1.875, 64, 100),  # Eb
    # Beat 4 (2.625)
    (2.625, 65, 100),  # F
    (2.625, 68, 100),  # A
    (2.625, 67, 100),  # C
    (2.625, 64, 100),  # Eb
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# SAX: One short motif — F (1), G (2), F (3), D (4)
# Start it, leave it hanging (rest on beat 1), return on beat 3

sax_notes = [
    (2.25, 65, 100),  # F (beat 3)
    (2.625, 67, 100), # D (beat 4)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

#---------------------
# BAR 3: FULL ENSEMBLE (repeat structure)
#---------------------

# BASS LINE: Repeat of same walking line
bass_notes = [
    (3.0, 65, 100),  # F (1)
    (3.375, 70, 100), # Bb (2)
    (3.75, 67, 100),  # C (3)
    (4.125, 69, 100), # E (4)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# PIANO: 7th chords on beat 2 and 4 again

piano_notes = [
    # Beat 2 (3.375)
    (3.375, 65, 100),  # F
    (3.375, 68, 100),  # A
    (3.375, 67, 100),  # C
    (3.375, 64, 100),  # Eb
    # Beat 4 (4.125)
    (4.125, 65, 100),  # F
    (4.125, 68, 100),  # A
    (4.125, 67, 100),  # C
    (4.125, 64, 100),  # Eb
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# SAX: Return to motif, now complete, but with a slight rest before the final note

sax_notes = [
    (3.75, 65, 100),  # F (beat 3)
    (3.75, 67, 100),  # G (beat 3)
    (4.125, 65, 100), # F (beat 4)
    (4.125, 62, 100), # D (beat 4)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

#---------------------
# BAR 4: FULL ENSEMBLE (BASS, PIANO, SAX)
#---------------------

# BASS LINE: Repeat of same walking line
bass_notes = [
    (4.5, 65, 100),  # F (1)
    (4.875, 70, 100), # Bb (2)
    (5.25, 67, 100),  # C (3)
    (5.625, 69, 100), # E (4)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# PIANO: 7th chords on beat 2 and 4 again

piano_notes = [
    # Beat 2 (4.875)
    (4.875, 65, 100),  # F
    (4.875, 68, 100),  # A
    (4.875, 67, 100),  # C
    (4.875, 64, 100),  # Eb
    # Beat 4 (5.625)
    (5.625, 65, 100),  # F
    (5.625, 68, 100),  # A
    (5.625, 67, 100),  # C
    (5.625, 64, 100),  # Eb
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.0625))

# SAX: Complete motif

sax_notes = [
    (5.25, 65, 100),  # F (beat 3)
    (5.25, 67, 100),  # G (beat 3)
    (5.625, 65, 100), # F (beat 4)
    (5.625, 62, 100), # D (beat 4)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

#---------------------
# Save the MIDI file
#---------------------

pm.write("jazz_intro_f_major.mid")
print("MIDI file saved as 'jazz_intro_f_major.mid'")
