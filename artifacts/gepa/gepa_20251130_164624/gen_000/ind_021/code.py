
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
bass_notes = [50, 51, 53, 55, 50, 49, 52, 55, 50, 51, 53, 55, 50, 49, 52, 55]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bars 2-4 = 3 bars of 4/4 = 3 * 4 = 12 beats
for bar in range(2, 5):
    time = bar * 1.5
    # Comp on 2 and 4
    for beat in [1, 3]:
        # Dm7
        for pitch in [50, 53, 55, 57]:
            piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + beat * 0.375, end=time + beat * 0.375 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, A -> D, F, Eb, A (repeat with slight variation)
motif = [50, 53, 52, 57]
sax_notes = []
for i, note in enumerate(motif):
    start = 1.5 + i * 0.375
    end = start + 0.375
    sax_notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))
# Repeat with slight variation
for i, note in enumerate(motif):
    start = 1.5 + (i + 4) * 0.375
    end = start + 0.375
    sax_notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))
# Add a resolution on the last note
sax_notes.append(pretty_midi.Note(velocity=110, pitch=50, start=1.5 + 8 * 0.375, end=1.5 + 8 * 0.375 + 0.25))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
