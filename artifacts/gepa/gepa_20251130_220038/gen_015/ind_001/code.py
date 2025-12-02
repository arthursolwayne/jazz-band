
import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Double Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes (MIDI note numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar at 160 BPM (60 / 160 = 0.375 seconds per beat, 1.5 seconds per bar)
BAR_DURATION = 1.5

# --- BAR 1: Drums only (0.0 - 1.5s) ---
# Build tension with kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
drum_notes = [
    (KICK, 0.0),    # Kick on beat 1
    (SNARE, 0.75),  # Snare on beat 2
    (KICK, 1.125),  # Kick on beat 3
    (SNARE, 1.875), # Snare on beat 4
    (HIHAT, 0.0),   # Hi-hat on 1 & 2
    (HIHAT, 0.375),
    (HIHAT, 0.75),
    (HIHAT, 1.125),
    (HIHAT, 1.5),
    (HIHAT, 1.875)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# --- BAR 2: Full ensemble (1.5 - 3.0s) ---

# Bass line (Marcus): Walking line in F minor, chromatic approaches
bass_notes = [
    (64, 1.5),     # F (root)
    (66, 1.875),   # Ab (chromatic passing)
    (65, 2.25),    # G (chord tone)
    (63, 2.625),   # E (chromatic passing)
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano chords (Diane): 7th chords on 2 & 4, comp on 2 and 4
# F7, Bb7, F7, Bb7
piano_notes = [
    (64, 1.5),     # F (F7 chord)
    (67, 1.5),     # A (F7)
    (69, 1.5),     # C (F7)
    (62, 1.5),     # Eb (F7)

    (67, 2.25),    # Bb (Bb7)
    (71, 2.25),    # D (Bb7)
    (69, 2.25),    # C (Bb7)
    (66, 2.25),    # Ab (Bb7)
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax melody (Dante): A short, haunting motif — F, Bb, G, Ab — each note held for 1 beat (0.375s)
sax_notes = [
    (64, 1.5),     # F
    (66, 1.875),   # Bb
    (65, 2.25),    # G
    (63, 2.625),   # Ab
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# --- BAR 3: Full ensemble (3.0 - 4.5s) ---

# Bass: Keep walking, chromatic approach
bass_notes = [
    (62, 3.0),     # Eb
    (63, 3.375),   # E
    (64, 3.75),    # F
    (65, 4.125),   # G
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Bb7 again, same as before
piano_notes = [
    (67, 3.0),     # Bb (Bb7)
    (71, 3.0),     # D (Bb7)
    (69, 3.0),     # C (Bb7)
    (66, 3.0),     # Ab (Bb7)
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Repeat the motif — F, Bb, G, Ab — but with a slight variation in the third bar to keep it evolving
sax_notes = [
    (64, 3.0),     # F
    (66, 3.375),   # Bb
    (63, 3.75),    # Ab
    (65, 4.125),   # G
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# --- BAR 4: Full ensemble (4.5 - 6.0s) ---

# Bass: Continue the walking line
bass_notes = [
    (67, 4.5),     # A
    (66, 4.875),   # Ab
    (64, 5.25),    # F
    (62, 5.625),   # Eb
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: F7 again, resolving the tension
piano_notes = [
    (64, 4.5),     # F (F7)
    (67, 4.5),     # A (F7)
    (69, 4.5),     # C (F7)
    (62, 4.5),     # Eb (F7)
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Return to the original motif, but slightly more resolved
sax_notes = [
    (64, 4.5),     # F
    (66, 4.875),   # Bb
    (65, 5.25),    # G
    (64, 5.625),   # F (resolve on root)
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# --- Drums in BAR 3 and BAR 4 (3.0 - 6.0s) ---
# Continue the kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * BAR_DURATION
    drum_notes = [
        (KICK, start_time),         # Kick on beat 1
        (SNARE, start_time + 0.75), # Snare on beat 2
        (KICK, start_time + 1.125), # Kick on beat 3
        (SNARE, start_time + 1.875),# Snare on beat 4
        (HIHAT, start_time),        # Hi-hat on 1 & 2
        (HIHAT, start_time + 0.375),
        (HIHAT, start_time + 0.75),
        (HIHAT, start_time + 1.125),
        (HIHAT, start_time + 1.5),
        (HIHAT, start_time + 1.875)
    ]

    for note, time in drum_notes:
        drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(drum_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
