
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Key: D Major
# Time signature: 4/4
# Duration: 6.0 seconds (160 BPM, 4 bars)
# Each bar is 1.5 seconds
# Beat duration: 0.375 seconds

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor sax
bass_instrument = pretty_midi.Instrument(program=33)  # Double bass
piano_instrument = pretty_midi.Instrument(program=0)   # Acoustic piano
drums_instrument = pretty_midi.Instrument(program=0)   # Drums

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drums_instrument]

# Time in seconds
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Define the sax melody — a short, singable motif
# Start on D (note number 62), move to F#, B, G# -> a simple, emotional line
sax_notes = [
    (62, 0.0),        # D4
    (66, 0.375),      # F#4
    (67, 0.75),       # G4
    (69, 1.125),      # A4
    (67, 1.5),        # G4
    (66, 1.875),      # F#4
    (62, 2.25),       # D4
    (69, 2.625),      # A4
    (67, 3.0),        # G4
    (66, 3.375),      # F#4
    (62, 3.75),       # D4
]

# Add sax notes
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax_instrument.notes.append(note_obj)

# Bass line: walking line, chromatic approaches
# Start on D (62), walk down, chromatic approaches in 4th bar
bass_notes = [
    (62, 0.0),        # D4
    (60, 0.375),      # B3 (chromatic approach)
    (59, 0.75),       # Bb3
    (62, 1.125),      # D4
    (64, 1.5),        # F4
    (62, 1.875),      # D4
    (60, 2.25),       # B3
    (59, 2.625),      # Bb3
    (62, 3.0),        # D4
    (64, 3.375),      # F4
    (62, 3.75),       # D4
    (60, 4.125),      # B3
    (59, 4.5),        # Bb3
    (62, 4.875),      # D4
]

# Add bass notes
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    bass_instrument.notes.append(note_obj)

# Piano chords: 7th chords, comping on 2 and 4
# D7 (62, 64, 67, 69) on 2 and 4
# Dm7 (62, 64, 67, 69) on 1 and 3

piano_notes = [
    # Bar 1: Dm7 on beat 1
    (62, 0.0), (64, 0.0), (67, 0.0), (69, 0.0),
    # Bar 1: rest
    # Bar 2: D7 on beat 2
    (62, 0.75), (64, 0.75), (67, 0.75), (69, 0.75),
    # Bar 2: rest
    # Bar 3: Dm7 on beat 3
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3: rest
    # Bar 4: D7 on beat 4
    (62, 2.25), (64, 2.25), (67, 2.25), (69, 2.25),
]

# Add piano notes
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano_instrument.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [(0, 0.0), (0, 1.5)]
snare_notes = [(1, 0.375), (1, 1.875)]
hihat_notes = [(42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
               (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125),
               (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625),
               (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125),
               (42, 3.0), (42, 3.1875), (42, 3.375), (42, 3.5625),
               (42, 3.75), (42, 3.9375), (42, 4.125), (42, 4.3125),
               (42, 4.5), (42, 4.6875), (42, 4.875), (42, 5.0625)]

# Add kick
for note, time in kick_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums_instrument.notes.append(note_obj)

# Add snare
for note, time in snare_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums_instrument.notes.append(note_obj)

# Add hihat
for note, time in hihat_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    drums_instrument.notes.append(note_obj)

# Save the MIDI file
pm.write("wayne_shorter_intro.mid")
