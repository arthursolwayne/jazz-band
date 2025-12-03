
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = []
bar_start = 1.5
for bar in range(3):
    # F7 (F, C, E, A) -> F, C, E, A
    # Chromatic approach to F
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_start + bar * 1.5, end=bar_start + bar * 1.5 + 0.375))
    # Root F
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_start + bar * 1.5 + 0.375, end=bar_start + bar * 1.5 + 0.75))
    # Fifth C
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=79, start=bar_start + bar * 1.5 + 0.75, end=bar_start + bar * 1.5 + 1.125))
    # Chromatic approach to A
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=80, start=bar_start + bar * 1.5 + 1.125, end=bar_start + bar * 1.5 + 1.5))
    
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = []
for bar in range(3):
    start = bar_start + bar * 1.5
    if bar == 0:
        # F7: F, A, C, E
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=84, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=79, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=81, start=start, end=start + 0.75))
    elif bar == 1:
        # B7: B, D#, F#, A
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=79, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=83, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=85, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=88, start=start, end=start + 0.75))
    elif bar == 2:
        # E7: E, G#, B, D
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=78, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=83, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=86, start=start, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=87, start=start, end=start + 0.75))

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(3):
    start = bar_start + bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar_start = 1.5
# Bar 2: Start the motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_start, end=bar_start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 0.375, end=bar_start + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125))
# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=100, pitch=78, start=bar_start + 1.5, end=bar_start + 1.875))
# Bar 4: Come back and finish it
sax_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 3.0, end=bar_start + 3.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 3.375, end=bar_start + 3.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 3.75, end=bar_start + 4.125))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
