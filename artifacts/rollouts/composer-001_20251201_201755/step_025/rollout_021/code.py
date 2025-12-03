
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
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
# Bar 2: Fm7 (F, Ab, D, Eb)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75))  # F
bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0))  # Ab
# Bar 3: Cm7 (C, Eb, G, Bb)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25))  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5))  # Bb
# Bar 4: Gm7 (G, Bb, D, F)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75))  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0))  # Ab
# Bar 5: Fm7 (F, Ab, D, Eb)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25))  # F
bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5))  # Ab
# Bar 6: Cm7 (C, Eb, G, Bb)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75))  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.0))  # Bb
# Bar 7: Gm7 (G, Bb, D, F)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25))  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=4.25, end=4.5))  # Ab
# Bar 8: Fm7 (F, Ab, D, Eb)
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75))  # F
bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=4.75, end=5.0))  # Ab
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
# Bar 2: Fm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.0))  # Ab
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0))  # Eb
# Bar 3: Cm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5))  # Eb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5))  # Bb
# Bar 4: Gm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0))  # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0))  # F
# Bar 5: Fm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.5))  # Ab
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5))  # Eb
# Bar 6: Cm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0))  # Eb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0))  # Bb
# Bar 7: Gm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5))  # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.5))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5))  # F
# Bar 8: Fm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=5.0))  # Ab
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0))  # Eb
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2: Start motif (F, Ab, Bb)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0))  # Ab
# Bar 3: Continue motif (D, C)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5))  # C
# Bar 4: Finish motif (F, Ab)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=2.75, end=3.0))  # Ab
# Bar 5: Repeat motif (F, Ab, Bb)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.5))  # Ab
# Bar 6: Continue motif (D, C)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75))  # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0))  # C
# Bar 7: Finish motif (F, Ab)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25))  # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=4.25, end=4.5))  # Ab
# Bar 8: Final note (Bb)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=5.0))  # Bb
sax.notes.extend(sax_notes)

# Drums: continue in bars 2-4
for i in range(2, 8):
    start = i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))
    else:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
