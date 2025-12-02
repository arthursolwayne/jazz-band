
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F major
key = 'F'

# Create instruments
instrument_drums = pretty_midi.Instrument(program=10)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

pm.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# Function to convert note name to MIDI number
def note_to_midi(note):
    return pretty_midi.note_name_to_midi(note, octave=3, enharmonic=0)

# Set time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Tempo is already set to 160 BPM, which is the default

# Define the 4 bars, each 6 seconds long
# Each bar = 1.5 seconds, beat = 0.375 seconds

# Bar 1: Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def bar1():
    # Kick on beats 1 and 3
    kick_notes = [note_to_midi('C4'), note_to_midi('C4')]
    kick_times = [0.0, 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    # Snare on beats 2 and 4
    snare_notes = [note_to_midi('C5'), note_to_midi('C5')]
    snare_times = [0.375, 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    # HiHat on every eighth
    hihat_notes = [note_to_midi('C6')] * 8
    hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
    for note, time in zip(hihat_notes, hihat_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
        instrument_drums.notes.append(note_event)

# Bar 2: Everyone enters — sax starts the melody
def bar2():
    # Bass: Walking line in F, chromatic approaches
    # F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F etc.
    # Translating to MIDI in F minor, but melody is simple and chromatic
    bass_notes = [note_to_midi('F2'), note_to_midi('G2'), note_to_midi('Ab2'), note_to_midi('A2'),
                  note_to_midi('Bb2'), note_to_midi('B2'), note_to_midi('C2'), note_to_midi('Db2'),
                  note_to_midi('D2'), note_to_midi('Eb2'), note_to_midi('E2'), note_to_midi('F2')]
    bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
    for note, time in zip(bass_notes, bass_times):
        note_event = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
        instrument_bass.notes.append(note_event)

    # Piano: 7th chords on 2 and 4, comp on beat 2 and 4
    # F7 = F, A, C, Eb — root, 3, 5, 7
    # F7: F, A, C, Eb
    # Bb7: Bb, D, F, Ab
    # Comp on beat 2 and 4 — 2 bars of 4/4
    # Bar 2: F7 on beat 2, Bb7 on beat 4
    # Bar 3: C7 on beat 2, G7 on beat 4 (but we're only doing 4 bars)
    # So we do F7 and Bb7 in bar 2
    for time, chord in [(0.375, ['F3', 'A3', 'C4', 'Eb4']), (1.125, ['Bb3', 'D4', 'F4', 'Ab4'])]:
        for note in chord:
            note_event = pretty_midi.Note(velocity=100, pitch=note_to_midi(note), start=time, end=time + 0.2)
            instrument_piano.notes.append(note_event)

    # Sax: Motif — simple, with tension and release
    # F, Ab, Bb, rest
    sax_notes = [note_to_midi('F4'), note_to_midi('Ab4'), note_to_midi('Bb4'), note_to_midi('Bb4')]
    sax_times = [0.0, 0.375, 0.75, 1.125]
    sax_durations = [0.375, 0.375, 0.375, 0.375]
    for note, time, duration in zip(sax_notes, sax_times, sax_durations):
        note_event = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
        instrument_sax.notes.append(note_event)

    # Drums: Continue the same pattern
    kick_notes = [note_to_midi('C4'), note_to_midi('C4')]
    kick_times = [0.0, 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    snare_notes = [note_to_midi('C5'), note_to_midi('C5')]
    snare_times = [0.375, 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    hihat_notes = [note_to_midi('C6')] * 8
    hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
    for note, time in zip(hihat_notes, hihat_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
        instrument_drums.notes.append(note_event)

# Bar 3: Continue the walking bass, piano comps, and sax continues motif
def bar3():
    # Bass: Walking line
    bass_notes = [note_to_midi('Bb2'), note_to_midi('B2'), note_to_midi('C2'), note_to_midi('Db2'),
                  note_to_midi('D2'), note_to_midi('Eb2'), note_to_midi('E2'), note_to_midi('F2'),
                  note_to_midi('F2'), note_to_midi('G2'), note_to_midi('Ab2'), note_to_midi('A2')]
    bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
    for note, time in zip(bass_notes, bass_times):
        note_event = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
        instrument_bass.notes.append(note_event)

    # Piano: 7th chords on beat 2 and 4
    for time, chord in [(1.875, ['C4', 'E4', 'G4', 'Bb4']), (2.625, ['G4', 'B4', 'D5', 'F5'])]:
        for note in chord:
            note_event = pretty_midi.Note(velocity=100, pitch=note_to_midi(note), start=time, end=time + 0.2)
            instrument_piano.notes.append(note_event)

    # Sax: Continue the motif
    sax_notes = [note_to_midi('F4'), note_to_midi('Ab4'), note_to_midi('Bb4'), note_to_midi('Bb4')]
    sax_times = [1.5, 1.875, 2.25, 2.625]
    sax_durations = [0.375, 0.375, 0.375, 0.375]
    for note, time, duration in zip(sax_notes, sax_times, sax_durations):
        note_event = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
        instrument_sax.notes.append(note_event)

    # Drums: Continue the pattern
    kick_notes = [note_to_midi('C4'), note_to_midi('C4')]
    kick_times = [1.5, 2.25]
    for note, time in zip(kick_notes, kick_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    snare_notes = [note_to_midi('C5'), note_to_midi('C5')]
    snare_times = [1.875, 2.625]
    for note, time in zip(snare_notes, snare_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    hihat_notes = [note_to_midi('C6')] * 8
    hihat_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
    for note, time in zip(hihat_notes, hihat_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
        instrument_drums.notes.append(note_event)

# Bar 4: End with a strong resolution, but leave it hanging — no answer
def bar4():
    # Bass: Walking line to end
    bass_notes = [note_to_midi('A2'), note_to_midi('Bb2'), note_to_midi('B2'), note_to_midi('C2')]
    bass_times = [3.0, 3.375, 3.75, 4.125]
    for note, time in zip(bass_notes, bass_times):
        note_event = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
        instrument_bass.notes.append(note_event)

    # Piano: Comp on beat 2 and 4
    for time, chord in [(3.375, ['F4', 'A4', 'C5', 'Eb5']), (4.125, ['F4', 'A4', 'C5', 'Eb5'])]:
        for note in chord:
            note_event = pretty_midi.Note(velocity=100, pitch=note_to_midi(note), start=time, end=time + 0.2)
            instrument_piano.notes.append(note_event)

    # Sax: Repeat the motif, but end on Bb4 and leave it hanging
    sax_notes = [note_to_midi('F4'), note_to_midi('Ab4'), note_to_midi('Bb4'), note_to_midi('Bb4')]
    sax_times = [3.0, 3.375, 3.75, 4.125]
    sax_durations = [0.375, 0.375, 0.375, 0.375]
    for note, time, duration in zip(sax_notes, sax_times, sax_durations):
        note_event = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
        instrument_sax.notes.append(note_event)

    # Drums: Continue the pattern
    kick_notes = [note_to_midi('C4'), note_to_midi('C4')]
    kick_times = [3.0, 3.75]
    for note, time in zip(kick_notes, kick_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    snare_notes = [note_to_midi('C5'), note_to_midi('C5')]
    snare_times = [3.375, 4.125]
    for note, time in zip(snare_notes, snare_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        instrument_drums.notes.append(note_event)

    hihat_notes = [note_to_midi('C6')] * 8
    hihat_times = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
    for note, time in zip(hihat_notes, hihat_times):
        note_event = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
        instrument_drums.notes.append(note_event)

# Build the 4 bars
bar1()
bar2()
bar3()
bar4()

# Save the MIDI file
pm.write('dante_intro.mid')
