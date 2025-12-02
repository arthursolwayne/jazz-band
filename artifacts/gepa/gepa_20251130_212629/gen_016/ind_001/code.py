
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument_track = pretty_midi.Instrument(program=64)  # Tenor Sax

# Set tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
pm.instruments = [instrument_track]

# Define the timing
BPM = 160
note_duration = 60 / BPM  # 0.375 seconds per beat
bar_duration = 4 * note_duration  # 1.5 seconds per bar
total_duration = 4 * bar_duration  # 6 seconds

# Set the key: D major (1 = D, 2 = E, 3 = F#, 4 = G, 5 = A, 6 = B, 7 = C#)
# MIDI notes: D4 = 62, E4 = 64, F#4 = 66, G4 = 67, A4 = 69, B4 = 71, C#5 = 73

# Bar 1: Little Ray (Drums) - Kick on 1 and 3, Snare on 2 and 4, Hihat on every 8th
# We won't model the drums here, but we'll leave space for them

# Bar 2: Diane (Piano) - 7th chords, comp on 2 and 4
# Bar 3: Marcus (Bass) - Walking line, chromatic approaches
# Bar 4: Dante (Tenor Sax) - Your motif

# Bar 1: Silence (drums only)
pass  # No sax in bar 1

# Bar 2: Diane's chords (7th chords on 2 and 4)
# We'll use piano track for this
piano_track = pretty_midi.Instrument(program=0)  # Piano
pm.instruments.append(piano_track)

# D7 chord: D, F#, A, C#
note_d = pretty_midi.Note(velocity=80, pitch=62, start=note_duration * 4, end=note_duration * 5)
note_fs = pretty_midi.Note(velocity=80, pitch=66, start=note_duration * 4, end=note_duration * 5)
note_a = pretty_midi.Note(velocity=80, pitch=69, start=note_duration * 4, end=note_duration * 5)
note_c = pretty_midi.Note(velocity=80, pitch=73, start=note_duration * 4, end=note_duration * 5)
piano_track.notes.extend([note_d, note_fs, note_a, note_c])

# Bar 3: Marcus's walking line (Bass)
bass_track = pretty_midi.Instrument(program=33)  # Bass
pm.instruments.append(bass_track)

# Walking line, chromatic approach to G (D, F#, G, A)
note_d_bass = pretty_midi.Note(velocity=80, pitch=46, start=note_duration * 6, end=note_duration * 7)
note_fs_bass = pretty_midi.Note(velocity=80, pitch=49, start=note_duration * 7, end=note_duration * 8)
note_g_bass = pretty_midi.Note(velocity=80, pitch=50, start=note_duration * 8, end=note_duration * 9)
note_a_bass = pretty_midi.Note(velocity=80, pitch=52, start=note_duration * 9, end=note_duration * 10)
bass_track.notes.extend([note_d_bass, note_fs_bass, note_g_bass, note_a_bass])

# Bar 4: Your motif (Tenor Sax)
# Start with a descending motif: D (62) to G (67), with a chromatic step in between
note_d_sax = pretty_midi.Note(velocity=100, pitch=62, start=note_duration * 10, end=note_duration * 11)
note_fs_sax = pretty_midi.Note(velocity=100, pitch=66, start=note_duration * 11, end=note_duration * 11.5)
note_g_sax = pretty_midi.Note(velocity=100, pitch=67, start=note_duration * 11.5, end=note_duration * 12)
instrument_track.notes.extend([note_d_sax, note_fs_sax, note_g_sax])

# Save the MIDI file
pm.write("wayne_intro.mid")
print("MIDI file generated: 'wayne_intro.mid'")
