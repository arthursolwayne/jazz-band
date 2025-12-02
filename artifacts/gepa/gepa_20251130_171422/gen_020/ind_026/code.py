
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
DRUM_KICK = 36
DRUM_SNARE = 38
DRUM_HIHAT = 42

# Bar 1 (0.0 - 1.5s): Little Ray on drums alone
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth

# Note duration is (60 / 160) * 1 = 0.375 seconds
note_duration = 0.375

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (DRUM_KICK, 0.0),
    (DRUM_SNARE, 0.375),
    (DRUM_KICK, 0.75),
    (DRUM_SNARE, 1.125),
    (DRUM_HIHAT, 0.0),
    (DRUM_HIHAT, 0.375),
    (DRUM_HIHAT, 0.75),
    (DRUM_HIHAT, 1.125),
    (DRUM_HIHAT, 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration)
    drums.notes.append(drum_note)

# Bar 2-4 (1.5 - 6.0s): Full quartet

# Bass line: Chromatic walking line in F, with 7th chords from Diane (comping on 2 and 4)
# Bass line: F, Gb, G, Ab, A, Bb, B, C (octave), etc.
# Let's play a walking line in F minor (F, Gb, G, Ab, A, Bb, B, C) for 3 bars (12 notes)

bass_notes = [
    (53, 1.5),  # F (3rd octave)
    (51, 1.875), # Gb
    (52, 2.25),  # G
    (50, 2.625), # Ab
    (55, 2.875), # A
    (54, 3.25),  # Bb
    (57, 3.625), # B
    (55, 3.875), # A (up)
    (53, 4.25),  # F
    (51, 4.625), # Gb
    (52, 5.0),   # G
    (50, 5.375)  # Ab
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on every 2 and 4, comping in F minor
# Chords: F7, Bb7, Ab7, Db7, etc.
# We'll just play F7 (F, A, C, Eb) on beat 2 and 4 for each bar

# Bar 2: F7 (beat 2 and 4)
piano_notes = [
    (53, 1.875), # F
    (58, 1.875), # A
    (55, 1.875), # C
    (51, 1.875), # Eb
    (53, 2.25), # F
    (58, 2.25), # A
    (55, 2.25), # C
    (51, 2.25), # Eb
]

# Bar 3: Bb7 (beat 2 and 4)
piano_notes += [
    (51, 3.125), # Bb
    (56, 3.125), # D
    (53, 3.125), # F
    (50, 3.125), # Ab
    (51, 3.5),   # Bb
    (56, 3.5),   # D
    (53, 3.5),   # F
    (50, 3.5),   # Ab
]

# Bar 4: Ab7 (beat 2 and 4)
piano_notes += [
    (50, 4.375), # Ab
    (55, 4.375), # C
    (52, 4.375), # Eb
    (49, 4.375), # Gb
    (50, 4.75),  # Ab
    (55, 4.75),  # C
    (52, 4.75),  # Eb
    (49, 4.75),  # Gb
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration)
    piano.notes.append(piano_note)

# Sax: Dante's motif. Start with a short, singing phrase in F minor
# Melody: F, Gb, G, C, B, A, G, F
# Timing: Starts at 1.5s, ends at 6.0s

sax_notes = [
    (53, 1.5),   # F
    (51, 1.875), # Gb
    (52, 2.25),  # G
    (55, 2.625), # C
    (57, 2.875), # B
    (55, 3.25),  # A
    (52, 3.625), # G
    (53, 4.0),   # F
    (55, 4.25),  # C (reprise)
    (57, 4.5),   # B (reprise)
    (55, 4.75),  # A (reprise)
    (53, 5.0)    # F (final note)
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + note_duration)
    sax.notes.append(sax_note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_shot.mid")
