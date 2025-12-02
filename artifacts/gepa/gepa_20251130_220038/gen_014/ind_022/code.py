
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2
for beat in range(4):
    time = 1.5 + beat * 0.375
    # Marcus: Walking bass line, chromatic approaches
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.25)
        bass.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + 0.25)
        bass.notes.append(note)

    # Diane: 7th chords, comp on 2 and 4
    if beat == 1 or beat == 3:
        if beat == 1:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)
        else:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)

    # Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

    # Dante: Melody - one short motif, make it sing
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=76, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=74, start=time, end=time + 0.25)
        sax.notes.append(note)

# Bar 3
for beat in range(4):
    time = 3.0 + beat * 0.375
    # Marcus: Walking bass line, chromatic approaches
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=73, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.25)
        bass.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + 0.25)
        bass.notes.append(note)

    # Diane: 7th chords, comp on 2 and 4
    if beat == 1 or beat == 3:
        if beat == 1:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)
        else:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)

    # Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

    # Dante: Melody - one short motif, make it sing
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=76, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=74, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=76, start=time, end=time + 0.25)
        sax.notes.append(note)

# Bar 4
for beat in range(4):
    time = 4.5 + beat * 0.375
    # Marcus: Walking bass line, chromatic approaches
    if beat == 0:
        note = pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.25)
        bass.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.25)
        bass.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + 0.25)
        bass.notes.append(note)

    # Diane: 7th chords, comp on 2 and 4
    if beat == 1 or beat == 3:
        if beat == 1:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)
        else:
            # F7
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=79, start=time, end=time + 0.25)
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=82, start=time, end=time + 0.25)
            piano.notes.append(note)

    # Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

    # Dante: Melody - one short motif, make it sing
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=76, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.25)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=74, start=time, end=time + 0.25)
        sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
