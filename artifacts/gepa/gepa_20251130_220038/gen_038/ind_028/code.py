
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375), # Bar 1
    (36, 0.75), (38, 1.125), (42, 1.125), # Bar 1
    (36, 1.5), (38, 1.875), (42, 1.875), # Bar 1
    (36, 2.25), (38, 2.625), (42, 2.625)  # Bar 1
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm (F, Eb, D, C, Bb, A, G, F#), chromatic approaches
bass_notes = [
    (64, 1.5), (62, 1.875), (61, 2.25), (60, 2.625),  # F, Eb, D, C
    (59, 3.0), (58, 3.375), (57, 3.75), (56, 4.125),  # Bb, A, G, F#
    (64, 4.5), (62, 4.875), (61, 5.25), (60, 5.625)   # F, Eb, D, C
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
piano_notes = [
    # Bar 2
    (64, 2.0), (69, 2.0), (60, 2.0), (64, 2.0),  # Fm7 on 2
    # Bar 3
    (70, 3.5), (73, 3.5), (64, 3.5), (69, 3.5),  # Bb7 on 4
    # Bar 4
    (64, 5.0), (69, 5.0), (60, 5.0), (64, 5.0)   # Fm7 on 2
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Dante - Melody in Fm, one short motif, make it sing
# Start with a whisper: F, Ab, D, Eb - then a cry: Gb, Bb, F, C
sax_notes = [
    # Bar 2
    (64, 1.5), (69, 1.5), (61, 1.5), (64, 1.5),  # F, Ab, D, C (half note)
    # Bar 3
    (64, 2.0), (69, 2.0), (61, 2.0), (64, 2.0),  # F, Ab, D, C (half note)
    # Bar 4
    (63, 3.0), (70, 3.0), (64, 3.0), (67, 3.0),  # Gb, Bb, F, C (half note)
    (64, 3.5), (69, 3.5), (61, 3.5), (64, 3.5)   # F, Ab, D, C (half note)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.5))

# Add the drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.25))
    # Add hihats on every eighth
    for i in range(8):
        hihat_time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125))

# Add the final fill at the end
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
