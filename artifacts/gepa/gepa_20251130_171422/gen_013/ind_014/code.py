
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=1.875 + 0.375),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.25 + 0.375),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=2.625 + 0.375),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=2.875 + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.25 + 0.375),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=3.625, end=3.625 + 0.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.0, end=4.0 + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.375, end=4.375 + 0.375),  # C#
    pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=4.75 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=75, start=5.125, end=5.125 + 0.375),  # D#
    pretty_midi.Note(velocity=80, pitch=76, start=5.5, end=5.5 + 0.375),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=5.875, end=5.875 + 0.375)   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, E♭
# B♭7: B♭, D, F, A♭
# C7: C, E, G, B♭
# E7: E, G#, B, D
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.1875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.1875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.1875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.25 + 0.1875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.1875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.1875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.1875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.25 + 0.1875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.25 + 0.1875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.25 + 0.1875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.25 + 0.1875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.375, end=4.375 + 0.1875),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.375, end=4.375 + 0.1875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.375, end=4.375 + 0.1875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.375 + 0.1875),  # A
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - A - B♭ - F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.5 + 0.1875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.6875, end=1.6875 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=1.875 + 0.1875),  # B♭
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.0625 + 0.1875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.5 + 0.1875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=2.6875, end=2.6875 + 0.1875),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=2.875, end=2.875 + 0.1875),  # B♭
    pretty_midi.Note(velocity=110, pitch=71, start=3.0625, end=3.0625 + 0.1875)  # F
]
sax.notes.extend(sax_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
