
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar at 160 BPM (seconds)
BAR_DURATION = 6.0 / 4  # 6 seconds for 4 bars, so 1.5 per bar
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds per beat

# Helper function to create a note
def note(note_number, start_time, duration):
    return pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=start_time + duration)

# Helper function to create a drum hit
def drum_hit(note_number, start_time):
    return pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=start_time + 0.1)

# Bar 1: ONLY drums (0.0 - 1.5s)
# Little Ray sets the mood: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_hits = [
    drum_hit(KICK, 0.0),
    drum_hit(SNARE, 0.375),
    drum_hit(KICK, 0.75),
    drum_hit(SNARE, 1.125),
    drum_hit(HIHAT, 0.0),
    drum_hit(HIHAT, 0.1875),
    drum_hit(HIHAT, 0.375),
    drum_hit(HIHAT, 0.5625),
    drum_hit(HIHAT, 0.75),
    drum_hit(HIHAT, 0.9375),
    drum_hit(HIHAT, 1.125),
    drum_hit(HIHAT, 1.3125),
]

drums.notes.extend(drum_hits)

# Bar 2: Full band enters
# Key: D minor (D, Eb, F, G, Ab, Bb, C)
# Time: 1.5s

# Bass line (Marcus): walking line, chromatic approaches
# Dm7: D, F, Ab, Bb
bass_line = [
    note(62, 1.5, 0.375),  # D
    note(64, 1.875, 0.375), # F
    note(61, 2.25, 0.375),  # Eb
    note(63, 2.625, 0.375), # F
    note(60, 2.999, 0.375), # D
    note(62, 3.374, 0.375), # F
    note(64, 3.75, 0.375),  # G
    note(61, 4.125, 0.375), # Eb
    note(63, 4.5, 0.375),   # F
    note(65, 4.875, 0.375), # G
    note(62, 5.25, 0.375),  # F
    note(60, 5.625, 0.375), # D
]

bass.notes.extend(bass_line)

# Piano (Diane): 7th chords, comp on 2 and 4
# Dm7: D, F, Ab, Bb
# Time: 1.5s
piano_notes = [
    note(62, 1.5, 0.375),  # D
    note(64, 1.5, 0.375),  # F
    note(67, 1.5, 0.375),  # Ab
    note(66, 1.5, 0.375),  # Bb

    note(62, 2.25, 0.375),  # D
    note(64, 2.25, 0.375),  # F
    note(67, 2.25, 0.375),  # Ab
    note(66, 2.25, 0.375),  # Bb

    note(62, 3.0, 0.375),   # D
    note(64, 3.0, 0.375),   # F
    note(67, 3.0, 0.375),   # Ab
    note(66, 3.0, 0.375),   # Bb

    note(62, 3.75, 0.375),  # D
    note(64, 3.75, 0.375),  # F
    note(67, 3.75, 0.375),  # Ab
    note(66, 3.75, 0.375),  # Bb
]

piano.notes.extend(piano_notes)

# Drums continue (Bar 2-4)
drum_hits = [
    drum_hit(KICK, 1.5),
    drum_hit(SNARE, 1.875),
    drum_hit(KICK, 2.25),
    drum_hit(SNARE, 2.625),
    drum_hit(HIHAT, 1.5),
    drum_hit(HIHAT, 1.6875),
    drum_hit(HIHAT, 1.875),
    drum_hit(HIHAT, 2.0625),
    drum_hit(HIHAT, 2.25),
    drum_hit(HIHAT, 2.4375),
    drum_hit(HIHAT, 2.625),
    drum_hit(HIHAT, 2.8125),

    drum_hit(KICK, 2.999),
    drum_hit(SNARE, 3.374),
    drum_hit(KICK, 3.75),
    drum_hit(SNARE, 4.125),
    drum_hit(HIHAT, 2.999),
    drum_hit(HIHAT, 3.1875),
    drum_hit(HIHAT, 3.374),
    drum_hit(HIHAT, 3.5625),
    drum_hit(HIHAT, 3.75),
    drum_hit(HIHAT, 3.9375),
    drum_hit(HIHAT, 4.125),
    drum_hit(HIHAT, 4.3125),

    drum_hit(KICK, 4.875),
    drum_hit(SNARE, 5.25),
    drum_hit(KICK, 5.625),
    drum_hit(SNARE, 6.0),
    drum_hit(HIHAT, 4.875),
    drum_hit(HIHAT, 5.0625),
    drum_hit(HIHAT, 5.25),
    drum_hit(HIHAT, 5.4375),
    drum_hit(HIHAT, 5.625),
    drum_hit(HIHAT, 5.8125),
    drum_hit(HIHAT, 6.0),
]

drums.notes.extend(drum_hits)

# Saxophone (Dante): short motif, start it, leave it hanging, come back and finish it
# Motif: D - F - Ab - Bb (Dm7), played as a short melodic phrase
# Bar 2: start the motif
# Bar 3: leave it hanging
# Bar 4: finish it

sax_notes = [
    note(62, 1.5, 0.375),  # D
    note(64, 1.875, 0.375), # F
    note(67, 2.25, 0.375),  # Ab
    note(66, 2.625, 0.375), # Bb

    # Leave it hanging
    note(62, 3.0, 0.375),   # D (rest the rest of the bar)
    note(62, 3.375, 0.375), # D
    note(62, 3.75, 0.375),  # D
    note(62, 4.125, 0.375), # D

    # Finish it
    note(62, 4.5, 0.375),   # D
    note(64, 4.875, 0.375), # F
    note(67, 5.25, 0.375),  # Ab
    note(66, 5.625, 0.375), # Bb
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.midi")
