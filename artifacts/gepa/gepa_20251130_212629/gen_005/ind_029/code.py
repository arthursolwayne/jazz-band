
import pretty_midi
import numpy as np

# Setup
tempo = 160
time_signature = (4, 4)
key = 'Dm'  # D Minor
note_duration = 0.25  # quarter note duration in seconds
bar_duration = 6.0  # 4 bars at 160 BPM = 6 seconds
sample_rate = 44100

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Create instruments
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)
sax = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Tenor Saxophone"))
piano = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Electric Piano 1"))
bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Double Bass"))

pm.instruments = [drums, sax, piano, bass]

# Time per beat (quarter note)
beat = 60.0 / tempo  # seconds per beat

# Bar 1: Drums only — tension and anticipation
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Create a 1-bar (4 beats) drum pattern
def add_drums(start_time):
    kick_notes = [26, 26]  # Kick on 1 and 3
    snare_notes = [38, 38]  # Snare on 2 and 4
    hihat_notes = [42] * 8  # Hihat on every eighth note

    for i, note in enumerate(kick_notes):
        drum_note = pretty_midi.Note(
            velocity=100, pitch=note, start=start_time + i * beat, end=start_time + i * beat + 0.1
        )
        drums.notes.append(drum_note)

    for i, note in enumerate(snare_notes):
        drum_note = pretty_midi.Note(
            velocity=95, pitch=note, start=start_time + i * beat, end=start_time + i * beat + 0.1
        )
        drums.notes.append(drum_note)

    for i, note in enumerate(hihat_notes):
        drum_note = pretty_midi.Note(
            velocity=80, pitch=note, start=start_time + i * beat / 2, end=start_time + i * beat / 2 + 0.05
        )
        drums.notes.append(drum_note)

# Add Bar 1 (Drums only)
add_drums(0.0)

# Bar 2: Sax enters with a short motif
def sax_motif(start_time):
    # Dm scale: D, Eb, F, G, Ab, Bb, C
    # Motif: D, F, Bb, Ab (ascending, then descending)
    # Using notes: D (D4), F (F4), Bb (Bb4), Ab (Ab4)
    notes = [62, 65, 70, 68]  # D4, F4, Bb4, Ab4
    velocities = [100, 105, 110, 105]
    durations = [note_duration, note_duration, note_duration, note_duration]

    for i, note in enumerate(notes):
        sax_note = pretty_midi.Note(
            velocity=velocities[i],
            pitch=note,
            start=start_time + i * note_duration,
            end=start_time + i * note_duration + durations[i]
        )
        sax.notes.append(sax_note)

# Bar 2: Sax enters with the motif
sax_motif(beat)  # starts on beat 1 of bar 2

# Bar 3: Bass enters with walking line (chromatic approaches)
def walking_bass(start_time):
    # Dm7 chord: D, F, Ab, C
    # Walking line: D, Eb, F, G, Ab, Bb, C, B (chromatic approach)
    notes = [62, 63, 65, 67, 68, 70, 72, 71]
    velocities = [80] * len(notes)
    durations = [note_duration] * len(notes)

    for i, note in enumerate(notes):
        bass_note = pretty_midi.Note(
            velocity=velocities[i],
            pitch=note,
            start=start_time + i * note_duration,
            end=start_time + i * note_duration + durations[i]
        )
        bass.notes.append(bass_note)

# Bar 3: Bass enters with walking line
walking_bass(beat * 2)  # starts on beat 1 of bar 3

# Bar 3: Piano enters with 7th chords, comp on 2 and 4
def piano_comp(start_time):
    # Dm7 chord: D, F, Ab, C (D7)
    # Comp on 2 and 4
    chords = [[62, 65, 68, 72], [62, 65, 68, 72]]  # Dm7 on beat 2 and 4
    durations = [note_duration / 2, note_duration / 2]

    for i, chord in enumerate(chords):
        for note in chord:
            piano_note = pretty_midi.Note(
                velocity=90,
                pitch=note,
                start=start_time + (i * 2 + 1) * note_duration,  # on beat 2 and 4
                end=start_time + (i * 2 + 1) * note_duration + durations[i]
            )
            piano.notes.append(piano_note)

# Bar 3: Piano enters
piano_comp(beat * 2)

# Bar 4: Sax returns with motif variation
def sax_motif_variation(start_time):
    # D, F, Bb, Ab -> Ab, Bb, F, D (descending)
    notes = [68, 70, 65, 62]  # Ab4, Bb4, F4, D4
    velocities = [105, 110, 105, 100]
    durations = [note_duration, note_duration, note_duration, note_duration]

    for i, note in enumerate(notes):
        sax_note = pretty_midi.Note(
            velocity=velocities[i],
            pitch=note,
            start=start_time + i * note_duration,
            end=start_time + i * note_duration + durations[i]
        )
        sax.notes.append(sax_note)

# Bar 4: Sax returns with variation
sax_motif_variation(beat * 3)

# Save the MIDI
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")
