
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125), # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75), # A#
    pretty_midi.Note(velocity=90, pitch=73, start=2.75, end=2.875), # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375), # G#
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # F#
    pretty_midi.Note(velocity=90, pitch=65, start=3.625, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875), # D#
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.0, end=4.125),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.25), # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.375), # B
    pretty_midi.Note(velocity=90, pitch=57, start=4.375, end=4.5),  # A#
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=4.625, end=4.75), # G#
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.0),  # F#
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75), # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75), # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.75), # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75), # Bb
    # Bar 2: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.375, end=2.5), # F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5), # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5), # C
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.75), # E
    # Bar 3: G7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5), # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5), # F#
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=69, start=3.625, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=73, start=3.625, end=3.75), # C#
    pretty_midi.Note(velocity=90, pitch=76, start=3.625, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.625, end=3.75), # G
    # Bar 4: B7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.5), # B
    pretty_midi.Note(velocity=90, pitch=75, start=4.375, end=4.5), # D#
    pretty_midi.Note(velocity=90, pitch=78, start=4.375, end=4.5), # F#
    pretty_midi.Note(velocity=90, pitch=81, start=4.375, end=4.5), # A
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - G - Bb - C (melodic minor) then repeat an octave higher
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75), # E
    pretty_midi.Note(velocity=100, pitch=79, start=2.75, end=2.875), # G
    pretty_midi.Note(velocity=100, pitch=83, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=88, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=100, pitch=91, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=95, start=3.375, end=3.5),  # Bb
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
