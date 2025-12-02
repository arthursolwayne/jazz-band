
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Create an instrument for each part
bass_program = pretty_midi.instrument_name_to_program('Upright Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)
pm.instruments.append(drums)

# BPM = 160 => quarter note = 0.375 seconds
# Bar = 4 quarter notes = 1.5 seconds
# 4 bars = 6 seconds

# Bar 1: Drums only
# Kick on 1 and 3, Snare on 2 and 4, Hi-hats on every eighth
def add_drums(bar_start, kick_notes, snare_notes, hi_hat_notes, instrument):
    for note in kick_notes:
        instrument.notes.append(pretty_midi.Note(
            velocity=80, pitch=note, start=bar_start + note, end=bar_start + note + 0.375
        ))
    for note in snare_notes:
        instrument.notes.append(pretty_midi.Note(
            velocity=80, pitch=note, start=bar_start + note, end=bar_start + note + 0.375
        ))
    for note in hi_hat_notes:
        instrument.notes.append(pretty_midi.Note(
            velocity=60, pitch=note, start=bar_start + note, end=bar_start + note + 0.125
        ))

# Bar 1: Drums
bar_1_start = 0
kick = [0.0]  # Kick on beat 1
snare = [0.5]  # Snare on beat 2
hi_hat = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]  # Every eighth

add_drums(bar_1_start, kick, snare, hi_hat, drums)

# Bar 2: Bass, Piano, Sax, Drums
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5

# Bass line - walking line in F minor
# Fm = F, Ab, Bb, D, Eb, G, Ab, Bb
# Walking line - chromatic approaches, no repeated notes
bass_notes = [
    (bar_2_start, 64, 0.5),    # F (64)
    (bar_2_start + 0.5, 63, 0.5),  # E (63)
    (bar_2_start + 1.0, 62, 0.5),  # Eb (62)
    (bar_2_start + 1.5, 60, 0.5),  # D (60)

    (bar_3_start, 60, 0.5),    # D
    (bar_3_start + 0.5, 62, 0.5),  # Eb
    (bar_3_start + 1.0, 63, 0.5),  # E
    (bar_3_start + 1.5, 64, 0.5),  # F

    (bar_4_start, 65, 0.5),    # F# (chromatic passing)
    (bar_4_start + 0.5, 62, 0.5),  # Eb
    (bar_4_start + 1.0, 60, 0.5),  # D
    (bar_4_start + 1.5, 59, 0.5)   # C (suspending the resolution)
]

for start, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Piano chords - 7th chords on 2 and 4, keeping the rhythm open
def add_piano_chord(start, chord, velocity=80):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.5))

# Fm7 on beat 2 (bar 2)
# Fm7 = F, Ab, Bb, D
add_piano_chord(bar_2_start + 0.5, [64, 63, 60, 62])

# Bb7 on beat 4 (bar 2)
# Bb7 = Bb, D, F, Ab
add_piano_chord(bar_2_start + 1.5, [60, 62, 64, 63])

# D7 on beat 2 (bar 3)
# D7 = D, F#, A, C
add_piano_chord(bar_3_start + 0.5, [60, 65, 67, 60])

# Gm7 on beat 4 (bar 3)
# Gm7 = G, Bb, D, F
add_piano_chord(bar_3_start + 1.5, [67, 60, 62, 64])

# C7 on beat 2 (bar 4)
# C7 = C, E, G, B
add_piano_chord(bar_4_start + 0.5, [60, 64, 67, 71])

# Leave bar 4's beat 4 open — anticipation, no resolution

# Sax part — your motif, short, melodic, with space and tension
sax_notes = [
    (bar_2_start + 0.25, 68, 0.5),  # G
    (bar_2_start + 0.75, 66, 0.25),  # F
    (bar_2_start + 1.0, 64, 0.5),   # E
    (bar_2_start + 1.5, 66, 0.25),  # F
    (bar_2_start + 1.75, 68, 0.5),  # G
    (bar_2_start + 2.25, 70, 0.25),  # A
    (bar_2_start + 2.5, 68, 0.25),  # G
    (bar_2_start + 2.75, 66, 0.25),  # F
    (bar_2_start + 3.0, 64, 0.25)   # E
]

for start, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Add hi-hats and snare again in bars 2–4
for bar_start in [bar_2_start, bar_3_start, bar_4_start]:
    kick = [bar_start]  # Kick on beat 1
    snare = [bar_start + 0.5]  # Snare on beat 2
    hi_hat = [bar_start + x * 0.125 for x in range(8)]  # Every eighth note

    for note in kick:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=bar_start + note, end=bar_start + note + 0.375))
    for note in snare:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=bar_start + note, end=bar_start + note + 0.375))
    for note in hi_hat:
        drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_start + note, end=bar_start + note + 0.125))

# Save the MIDI file
pm.write('jazz_intro.mid')

print("MIDI file created: jazz_intro.mid")
