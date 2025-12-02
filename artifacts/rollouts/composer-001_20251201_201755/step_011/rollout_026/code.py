
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on 1& 
    (36, 0.75, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on 3&
    (38, 1.5, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# 2nd Bar (1.5 - 3.0s)
# Marcus (Bass) - Walking line in Fm (F, Ab, D, Eb, etc.)
bass_notes = [
    (43, 1.5, 0.375),  # D2 (Fm root + 5)
    (41, 1.875, 0.375),  # Bb2 (Fm root + 3)
    (43, 2.25, 0.375),  # D2 (Fm root + 5)
    (42, 2.625, 0.375)   # C2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane (Piano) - Open voicings, resolve on the last
piano_notes = [
    (48, 1.5, 0.375),  # C4 (Fm7)
    (50, 1.5, 0.375),  # D4
    (53, 1.5, 0.375),  # F#4
    (55, 1.5, 0.375),  # A4
    (46, 2.25, 0.375),  # E3 (Fm7)
    (48, 2.25, 0.375),  # G3
    (50, 2.25, 0.375),  # A3
    (52, 2.25, 0.375),  # B3
    (55, 3.0, 0.375),  # A4 (Fm7)
    (53, 3.0, 0.375),  # F#4
    (50, 3.0, 0.375),  # D4
    (48, 3.0, 0.375)   # C4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125))

# Dante (Sax) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # E4 (start of motif)
    (64, 1.875, 0.375),  # F#4
    (62, 2.25, 0.375),  # E4 (end of first phrase)
    (65, 3.0, 0.375),  # G4 (return to finish motif)
    (62, 3.375, 0.375),  # E4
    (61, 3.75, 0.375)   # D4 (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_shorter_intro.mid')
