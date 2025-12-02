
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor (F, Gb, Ab, Bb, B, Db, Eb)
key = 'F minor'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Add the time signature
pm.time_signature_changes.append(time_signature)

# Create instruments
# 1. Marcus - Bass (walking line)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

# 2. Diane - Piano (comping)
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano = pretty_midi.Instrument(program=piano_program)

# 3. Little Ray - Drums
drum_program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = pretty_midi.Instrument(program=drum_program)

# 4. Dante Russo - Tenor Sax
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Tempo: 160 BPM
# One beat = 0.375s
# One bar = 1.5s
# Total length: 6.0 seconds

#----------------------------
# BAR 1: Little Ray alone (Drums)
#----------------------------

# Kick on 1 and 3
kick_times = [0.0, 1.5]
kick_notes = [36] * len(kick_times)  # MIDI note for kick (C2)
for t, n in zip(kick_times, kick_notes):
    kick = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4
snare_times = [0.75, 2.25]
snare_notes = [38] * len(snare_times)  # MIDI note for snare (D2)
for t, n in zip(snare_times, snare_notes):
    snare = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth note
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
hihat_notes = [42] * len(hihat_times)  # MIDI note for hi-hat (F2)
for t, n in zip(hihat_times, hihat_notes):
    hihat = pretty_midi.Note(velocity=90, pitch=n, start=t, end=t + 0.08)
    drums.notes.append(hihat)

#----------------------------
# BAR 2: All in (Bass, Piano, Sax)
#----------------------------

# Marcus: Walking bass line (chromatic approaches, no repeated notes)
# Fm7: F, Ab, Bb, Db
# Bass line: F, Gb, Ab, Bb, B, Db, Eb, F (chromatic descent)
bass_notes = [53, 51, 55, 56, 59, 59, 60, 53]  # MIDI notes (F3 to F4)
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for t, n in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.25)
    bass.notes.append(note)

# Diane: Piano comping on 2 and 4
# Fm7 chord: F, Ab, Bb, Db
# Comp on 2 and 4
comp_notes = [53, 55, 56, 59]  # F3, Ab3, Bb3, Db4
comp_times = [2.25, 3.75]
for t in comp_times:
    for n in comp_notes:
        note = pretty_midi.Note(velocity=90, pitch=n, start=t, end=t + 0.5)
        piano.notes.append(note)

# Dante: Tenor Sax motif — start it, leave it hanging
# Motif: F, Ab, Bb, Db (Fm7 arpeggio, starting with F)
# But with unique timing and dynamic variation
sax_notes = [53, 55, 56, 59]
sax_times = [1.5, 1.8, 2.0, 2.15]  # Delayed, spaced out
sax_velocities = [85, 90, 100, 80]  # Dynamic variation
for t, n, v in zip(sax_times, sax_notes, sax_velocities):
    note = pretty_midi.Note(velocity=v, pitch=n, start=t, end=t + 0.1)
    sax.notes.append(note)

#----------------------------
# BAR 3 & 4: Continue the motif with resolution (sax)
#----------------------------

# Continue the motif with a slight resolution or return to the motif
# Second phrase: same motif, but with slight variation in timing or dynamics
sax_notes_2 = [53, 55, 56, 59]
sax_times_2 = [3.0, 3.25, 3.5, 3.7]
sax_velocities_2 = [80, 95, 100, 90]
for t, n, v in zip(sax_times_2, sax_notes_2, sax_velocities_2):
    note = pretty_midi.Note(velocity=v, pitch=n, start=t, end=t + 0.1)
    sax.notes.append(note)

#----------------------------
# Write the MIDI file
#----------------------------

pm.write('dante_intro_fm.mid')
print("MIDI file written as 'dante_intro_fm.mid'")
