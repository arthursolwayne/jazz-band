
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 (D-F-A-C)
bass_note = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to G (43)
bass_note = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.375, end=1.5 + 0.375 + 0.375)
bass.notes.append(bass_note)
# Root G (43)
bass_note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to D (38)
bass_note = pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375)
bass.notes.append(bass_note)

# Bar 3: G7 (G-B-D-F)
bass_note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to B (46)
bass_note = pretty_midi.Note(velocity=90, pitch=45, start=1.5 + 1.5 + 0.375, end=1.5 + 1.5 + 0.375 + 0.375)
bass.notes.append(bass_note)
# Root B (46)
bass_note = pretty_midi.Note(velocity=90, pitch=46, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 0.75 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to G (43)
bass_note = pretty_midi.Note(velocity=90, pitch=44, start=1.5 + 1.5 + 1.125, end=1.5 + 1.5 + 1.125 + 0.375)
bass.notes.append(bass_note)

# Bar 4: Cm7 (C-Eb-G-Bb)
bass_note = pretty_midi.Note(velocity=90, pitch=40, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to Eb (43)
bass_note = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 3.0 + 0.375, end=1.5 + 3.0 + 0.375 + 0.375)
bass.notes.append(bass_note)
# Root Eb (43)
bass_note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 3.0 + 0.75, end=1.5 + 3.0 + 0.75 + 0.375)
bass.notes.append(bass_note)
# Chromatic approach to C (40)
bass_note = pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 3.0 + 1.125, end=1.5 + 3.0 + 1.125 + 0.375)
bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375)
piano.notes.append(piano_note)

# Bar 3: G7 (G-B-D-F)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
piano.notes.append(piano_note)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=63, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> Eb (63) -> D (62) -> C (60)
# Bar 2: Start the motif
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=63, start=1.5 + 0.375, end=1.5 + 0.375 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
sax.notes.append(sax_note)
# Bar 3: Leave it hanging for a beat
# Bar 4: Come back and finish it
sax_note = pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
