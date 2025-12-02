
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 4/4 time, 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_bass = pretty_midi.Instrument(program=33)  # Bass
track_piano = pretty_midi.Instrument(program=0)  # Piano
track_drums = pretty_midi.Instrument(program=11)  # Drums
track_sax = pretty_midi.Instrument(program=64)   # Tenor Sax

# Time per bar: 6 seconds / 4 bars = 1.5 seconds/bar
# Time per beat: 1.5 / 4 = 0.375 seconds/beat
# Time per note (quarter note): 0.375 seconds

# Create a time array for the 4 bars (160 BPM, 4/4, 4 bars = 16 beats)
time_per_beat = 0.375
times = np.arange(0, 4 * 4 * time_per_beat, time_per_beat)

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    beat = i * 4
    # Kick on 1 and 3
    kick_beats = [beat + 0, beat + 2]
    for kick in kick_beats:
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,
            start=kick * time_per_beat,
            end=(kick + 0.05) * time_per_beat
        )
        track_drums.notes.append(note)
    
    # Snare on 2 and 4
    snare_beats = [beat + 1, beat + 3]
    for snare in snare_beats:
        note = pretty_midi.Note(
            velocity=100,
            pitch=38,
            start=snare * time_per_beat,
            end=(snare + 0.05) * time_per_beat
        )
        track_drums.notes.append(note)
    
    # Hihat on every eighth
    for e in range(8):
        note = pretty_midi.Note(
            velocity=80,
            pitch=42,
            start=(beat + e/2) * time_per_beat,
            end=(beat + e/2 + 0.025) * time_per_beat
        )
        track_drums.notes.append(note)

# --- BASS: Marcus ---
# Walking line, chromatic approaches, no repeated notes
bass_notes = [
    50, 49, 51, 52, 51, 50, 48, 47,  # Dm7 (D, C#, F, G)
    49, 50, 48, 47, 49, 50, 48, 47,  # Dm7
    49, 50, 48, 47, 51, 52, 51, 50,  # Dm7
    49, 50, 48, 47, 49, 50, 48, 47   # Dm7
]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(
        velocity=80,
        pitch=pitch,
        start=i * time_per_beat,
        end=(i + 1) * time_per_beat
    )
    track_bass.notes.append(note)

# --- PIANO: Diane ---
# 7th chords, comp on 2 and 4
def dm7_chords():
    return [50, 52, 55, 57]  # Dm7 (D, F, A, C)

for i in range(4):
    beat = i * 4
    # Chord on 2 and 4 (beat 1 and 3 in measure)
    for j in [1, 3]:
        chord_start = (beat + j) * time_per_beat
        for pitch in dm7_chords():
            note = pretty_midi.Note(
                velocity=90,
                pitch=pitch,
                start=chord_start,
                end=chord_start + 0.5
            )
            track_piano.notes.append(note)

# --- SAX: Dante ---
# Melody: A haunting, unresolved motif
# Melody notes in Dm (D, E♭, F, G, A, B♭, C, D)
# Motif: D - F - G - B♭ (ascending 6th with a chromatic twist)

sax_notes = [
    50,  # D
    52,  # E
    51,  # F (chromatic descent)
    53,  # F# (chromatic lead)
    55,  # G
    57,  # A
    55,  # G
    54,  # G# (chromatic lead)
    50,  # D
    52,  # E
    51,  # F (chromatic descent)
    53,  # F# (chromatic lead)
    55,  # G
    57,  # A
    55,  # G
    54   # G# (chromatic lead)
]

for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(
        velocity=105,
        pitch=pitch,
        start=i * time_per_beat,
        end=(i + 0.5) * time_per_beat
    )
    track_sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [track_drums, track_bass, track_piano, track_sax]

# Save the MIDI file
midi.write("dante_sax_intro.mid")
print("MIDI file saved as 'dante_sax_intro.mid'")
