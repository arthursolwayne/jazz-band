
import pretty_midi

# Initialize MIDI file with tempo
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

# Time in seconds per bar (160 BPM, 4/4 time)
BAR_DURATION = 1.5

# -----------------------------
# BAR 1: DRUMS ONLY (0.0 - 1.5s)
# -----------------------------
# Little Ray sets the mood with syncopated, sparse rhythm
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (KICK, 0.0), 
    (SNARE, 0.5), 
    (KICK, 1.0), 
    (SNARE, 1.5),
    (HIHAT, 0.0),
    (HIHAT, 0.25),
    (HIHAT, 0.5),
    (HIHAT, 0.75),
    (HIHAT, 1.0),
    (HIHAT, 1.25),
    (HIHAT, 1.5),
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(drum_note)

# -----------------------------
# BAR 2: INTRO — FULL QUARTET (1.5 - 3.0s)
# -----------------------------
# SAX: Begin the motif — a short, questioning phrase
sax_notes = [
    (62, 1.5),  # F4 (root of Fm)
    (64, 1.75), # Ab4 (minor third)
    (66, 2.0),  # Bb4 (diminished fifth)
    (64, 2.25), # Ab4 (back)
    (62, 2.5),  # F4 (resolve)
    (60, 2.75), # D4 (lower third)
    (62, 3.0),  # F4 (return)
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# BASS: Walking line in Fm with chromatic approaches
bass_notes = [
    (38, 1.5),  # F2 (root)
    (37, 1.75), # Eb2 (chromatic approach)
    (39, 2.0),  # G2 (fifth)
    (40, 2.25), # Ab2 (chromatic)
    (38, 2.5),  # F2
    (37, 2.75), # Eb2
    (39, 3.0),  # G2
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# PIANO: Open voicings, resolving on the last bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (62, 1.5),  # F4
    (64, 1.5),  # Ab4
    (67, 1.5),  # C5
    (66, 1.5),  # Bb4 (dominant 7th, but we’re in Fm)
    (64, 1.75), # Ab4 (hold)
    (67, 1.75), # C5
    (66, 1.75), # Bb4
    (62, 2.0),  # F4 (resolve)
    (64, 2.0),  # Ab4
    (67, 2.0),  # C5
    (66, 2.0),  # Bb4
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# -----------------------------
# BAR 3: CONTINUING THE SAX MOTIF (3.0 - 4.5s)
# -----------------------------
# Repeat and variation of the sax motif
sax_notes = [
    (62, 3.0),  # F4
    (64, 3.25), # Ab4
    (66, 3.5),  # Bb4
    (64, 3.75), # Ab4
    (62, 4.0),  # F4
    (60, 4.25), # D4
    (62, 4.5),  # F4
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# BASS: Walking line in Fm with chromatic approaches
bass_notes = [
    (38, 3.0),  # F2
    (37, 3.25), # Eb2
    (39, 3.5),  # G2
    (40, 3.75), # Ab2
    (38, 4.0),  # F2
    (37, 4.25), # Eb2
    (39, 4.5),  # G2
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# PIANO: Fm7 (F, Ab, C, D) on beat 2, Bbm7 (Bb, Db, F, G) on beat 4
piano_notes = [
    (62, 3.0),  # F4
    (64, 3.0),  # Ab4
    (67, 3.0),  # C5
    (66, 3.0),  # Bb4 (Fm7)
    (64, 3.5),  # Ab4
    (67, 3.5),  # C5
    (66, 3.5),  # Bb4
    (64, 3.75), # Ab4 (hold)
    (67, 3.75), # C5
    (66, 3.75), # Bb4
    (62, 4.0),  # F4
    (64, 4.0),  # Ab4
    (67, 4.0),  # C5
    (66, 4.0),  # Bb4
    (64, 4.25), # Ab4
    (67, 4.25), # C5
    (66, 4.25), # Bb4
    (62, 4.5),  # F4
    (64, 4.5),  # Ab4
    (67, 4.5),  # C5
    (66, 4.5),  # Bb4
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# -----------------------------
# BAR 4: RESOLUTION (4.5 - 6.0s)
# -----------------------------
# SAX: Finish the motif with a twist — to the 9th
sax_notes = [
    (62, 4.5),  # F4
    (64, 4.75), # Ab4
    (66, 5.0),  # Bb4
    (68, 5.25), # C5 (the 9th)
    (66, 5.5),  # Bb4
    (64, 5.75), # Ab4
    (62, 6.0),  # F4
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# BASS: Finish the walking line
bass_notes = [
    (38, 4.5),  # F2
    (37, 4.75), # Eb2
    (39, 5.0),  # G2
    (40, 5.25), # Ab2
    (38, 5.5),  # F2
    (37, 5.75), # Eb2
    (39, 6.0),  # G2
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# PIANO: End on Fm7 (F, Ab, C, D)
piano_notes = [
    (62, 4.5),  # F4
    (64, 4.5),  # Ab4
    (67, 4.5),  # C5
    (66, 4.5),  # Bb4
    (64, 4.75), # Ab4
    (67, 4.75), # C5
    (66, 4.75), # Bb4
    (62, 5.0),  # F4
    (64, 5.0),  # Ab4
    (67, 5.0),  # C5
    (66, 5.0),  # Bb4
    (64, 5.25), # Ab4
    (67, 5.25), # C5
    (66, 5.25), # Bb4
    (62, 5.5),  # F4
    (64, 5.5),  # Ab4
    (67, 5.5),  # C5
    (66, 5.5),  # Bb4
    (64, 5.75), # Ab4
    (67, 5.75), # C5
    (66, 5.75), # Bb4
    (62, 6.0),  # F4
    (64, 6.0),  # Ab4
    (67, 6.0),  # C5
    (66, 6.0),  # Bb4
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums for bar 4 (same pattern as bar 1)
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time + 3.0, end=time + 3.25)
    drums.notes.append(drum_note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
