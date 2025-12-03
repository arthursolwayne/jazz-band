
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
# Hi-hats on every eighth
for i in range(0, 4):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=(i+1)*0.375))
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2-C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=90, pitch=74, start=1.625, end=1.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=1.875),  # C3 (F5)
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0),  # B2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, G#, Bb, Ab (melodic fragment)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125),  # F2
    pretty_midi.Note(velocity=90, pitch=74, start=3.125, end=3.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=77, start=3.25, end=3.375),  # C3 (F5)
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.5),  # B2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - C, D, Bb, F (resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=74, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.625),  # F2
    pretty_midi.Note(velocity=90, pitch=74, start=4.625, end=4.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=4.875),  # C3 (F5)
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),  # B2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution - F, G#, Bb, F (emphasize the F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3-4 (same pattern as bar 1)
for i in range(0, 4):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375+3.0, end=(i+1)*0.375+3.0))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
