
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note values
# Fm7 = F, Ab, C, Eb
# Chromatic walk on bass
# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (42, 0.0), (36, 0.375), (42, 0.375),
    (38, 0.75), (42, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (42, 1.5),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Chromatic walk starting from F
bass_notes = [
    # Bar 2
    (84, 1.5), (85, 1.875), (83, 2.25), (82, 2.625),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
# Fm7 = F, Ab, C, Eb
piano_notes = [
    # Bar 2
    (71, 1.5), (76, 1.5), (78, 1.5), (74, 1.5),
    # Bar 3
    (71, 3.0), (76, 3.0), (78, 3.0), (74, 3.0),
    # Bar 4
    (71, 4.5), (76, 4.5), (78, 4.5), (74, 4.5),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: Motif in Fm
# Fm minor scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Bb - Ab - Gb (hanging on Bb)
sax_notes = [
    # Bar 2
    (71, 1.5), (74, 1.875), (76, 2.25), (73, 2.625),
    # Bar 3
    (74, 3.0), (73, 3.375),
    # Bar 4
    (76, 4.5), (71, 4.875),
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick_times = [start_time, start_time + 0.75]
    # Snare on 2 and 4
    snare_times = [start_time + 0.375, start_time + 1.125]
    # Hihat on every eighth
    for t in [0.0, 0.375, 0.75, 1.125]:
        hihat_time = start_time + t
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125))
    for t in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
    for t in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
